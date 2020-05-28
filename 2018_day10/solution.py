#!/usr/bin/env python

# steps
# parse input
# array of objects
# visualize step
# check if visible
import re

class Star:
    def __init__(self, x_pos, y_pos, x_vel, y_vel):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_vel = x_vel
        self.y_vel = y_vel

    def print(self):
        print("Star params: x_pos: {}, y_pos: {}, x_vel: {}, y_vel: {}".format(self.x_pos, self.y_pos, self.x_vel, self.y_vel))

    def move(self):
        self.x_pos += self.x_vel
        self.y_pos += self.y_vel

class Sky:
    def __init__(self, input, max_iterations):
        self.input = input
        self.max_iterations = max_iterations
    
    stars = []

    def parse_input(self):
        with open(self.input, 'r') as f:
            lines = f.readlines()
        
        for line in lines:
            values = re.search('^position=<\s*([-\d]+),\s*([-\d]+)> velocity=<(\s*[-\d]+),\s*([-\d]*)>$', line, re.IGNORECASE)
            
            if values is not None:
                star = Star(int(values.group(1)), int(values.group(2)), int(values.group(3)), int(values.group(4)))
                star.print()

                self.stars.append(star)

    def message_in_the_sky(self):
        rem_iterations = self.max_iterations

        while not self.can_read_message() and rem_iterations > 0:
            bound_left = 10000000
            bound_right = -10000000
            bound_down = 10000000
            bound_top = -100000000

            for star in self.stars:
                bound_left = min(bound_left, star.x_pos)
                bound_right = max(bound_right, star.x_pos)
                bound_down = min(bound_down, star.y_pos)
                bound_top = max(bound_top, star.y_pos)

            if self.is_visible(bound_left, bound_right, bound_top, bound_down):
                self.print_stars(bound_left, bound_right, bound_top, bound_down)
            else:
                print("Cannot print the sky...")

            for star in self.stars:
                # print("before move")
                # star.print()
                # print("after move")
                star.move() 

                # star.print()

            rem_iterations -= 1

    def is_visible(self, bound_left, bound_right, bound_down, bound_top):
        print("Bounding box: {}, {}, {}, {}".format(bound_left, bound_right, bound_top, bound_down))
        if bound_right - bound_left + 1 + 4 <= 1000 and bound_down - bound_top + 1 + 4 <= 1000:
            return True
        else:
            print("Sky dimensions: {} : {}".format(bound_right - bound_left + 1 + 4, bound_down - bound_top + 1 + 4))
            return False

    def can_read_message(self):
        return False

    def print_stars(self, bound_left, bound_right, bound_top, bound_down):
        # fill with dots
        sky_board = [ [ '. ' for col in range(bound_right - bound_left + 1 + 4)] for row in range(bound_down - bound_top + 1 + 4) ]

        for star in self.stars:
            print("Star position: {} {}".format(star.x_pos, star.y_pos))
            print("Bounding box position: {} {}".format(star.x_pos - bound_left - 1, star.y_pos - bound_top - 1))
            sky_board[star.y_pos - bound_top + 2][star.x_pos - bound_left + 2] = '# '

        print("{}, {}".format(len(sky_board), len(sky_board[0])), file=f)

        for row in range(len(sky_board)):
            for col in range(len(sky_board[0])):
                print(sky_board[row][col], end='', file=f)
            print('\n', file=f)

def main():
    sky = Sky("test.txt", 10)

    sky.parse_input()
    print(len(sky.stars))
    assert len(sky.stars) == 31, "test failed, should be 31"
    print("Run the test first:")
    #assert "hi" == sky.message_in_the_sky(), "test failed, the message should be hi"

    print("Main input: ")
    sky = Sky("input.txt", 1000000)
    sky.parse_input()
    print(len(sky.stars))
    
    assert "hi" == sky.message_in_the_sky(), "test failed, the message should be hi"


if __name__ == '__main__':
    main()
