#!/usr/bin/env python

import sys

"""
This is a solution to the Code of Advent challenge
https://adventofcode.com/2018/day/10
====================

:Example:
>>> python solution.py

Main steps:
1) parse input
2) array of Star objects
3) visualize step
4) check if visible
"""

import re

class Star:
    """ Class that represents the Sky full of stars. """
    
    def __init__(self, x_pos, y_pos, x_vel, y_vel):
        """ 
        Default constructor
        :param x_pos: X Position
        :param y_pos: y Position
        :param x_vel: X velocity
        :param y_vel: Y velocity
        """
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_vel = x_vel
        self.y_vel = y_vel

    def print(self):
        """
        Prints the star information
        """
        print("Star params: x_pos: {}, y_pos: {}, x_vel: {}, y_vel: {}"
            .format(self.x_pos, self.y_pos, self.x_vel, self.y_vel))

    def move(self):
        """
        Moves the star according to its paremeters
        """
        self.x_pos += self.x_vel
        self.y_pos += self.y_vel

class Sky:
    """
    Object that represents Sky full of Stars
    """

    def __init__(self, input, max_iterations, bounding_box_width = 100, 
        bounding_box_height = 100):
        """
        Default Constructor
        :param input: path to the input txt file
        :param max_iterations: number of max iterations to be evaluated
        :param bounding_box_width: how big is the bounding box (width)
        :param bounding_box_height: how big is the bounding box (height)
        """

        self.input = input
        self.stars = []
        self.max_iterations = max_iterations
        self.bounding_box_width = bounding_box_width
        self.bounding_box_height = bounding_box_height

    def parse_input(self):
        """
        Parse the input file
        """

        with open(self.input, 'r') as f:
            lines = f.readlines()
        
        for line in lines:
            values = re.search('^position=<\s*([-\d]+),\s*([-\d]+)> velocity=<(\s*[-\d]+),\s*([-\d]*)>$', line, re.IGNORECASE)
            
            if values is not None:
                star = Star(int(values.group(1)), int(values.group(2)), 
                    int(values.group(3)), int(values.group(4)))
                self.stars.append(star)

    def message_in_the_sky(self):
        """
        Main loop, iterate over time and move stars in the sky
        """

        rem_iterations = self.max_iterations

        while not self.can_read_message() and rem_iterations > 0:
            bound_left = sys.maxsize
            bound_right = -sys.maxsize
            bound_top = sys.maxsize
            bound_down = -sys.maxsize
            
            for star in self.stars:
                bound_left = min(bound_left, star.x_pos)
                bound_right = max(bound_right, star.x_pos)
                bound_top = min(bound_top, star.y_pos)
                bound_down = max(bound_down, star.y_pos)

            if self.is_visible(bound_left, bound_right, bound_top, bound_down):
                print("{} seconds have elapsed".format(self.max_iterations - rem_iterations + 1))
                self.print_stars(bound_left, bound_right, bound_top, bound_down)

            for star in self.stars:
                star.move()

            rem_iterations -= 1

    def is_visible(self, bound_left, bound_right, bound_top, bound_down):
        """
        Function that determines if the current constellation is visible 
        (the bounding box is small enough to reason about the constelation)
        """

        if (bound_right - bound_left + 1 + 4 <= self.bounding_box_width 
                and bound_down - bound_top + 1 + 4 <= self.bounding_box_height):
            return True
        else:
            return False

    def can_read_message(self):
        """
        Placeholder function that would reason if the text can be read
        """
        return False

    def print_stars(self, bound_left, bound_right, bound_top, bound_down):
        """
        Function that prints the stars in ASCI format
        :param bound_left: left coordinates of bounding box
        :param bound_right: right coordinates of bounding box
        :param bound_top: top coordinates of bounding box
        :param bound_down: down coordinates of bounding box
        """
        
        # fill with dots
        sky_board = [ [ '. ' for col in range(bound_right - bound_left + 1 + 4)] 
            for row in range(bound_down - bound_top + 1 + 4) ]

        for star in self.stars:
            # put a star symbol
            sky_board[star.y_pos - bound_top + 2][star.x_pos - bound_left + 2] = '# '   

        print("Size of the sky (bounding box): width: {}, length: {}".format(len(sky_board[0]), 
            len(sky_board)))

        # iterate over sky board
        for row in range(len(sky_board)):
            for col in range(len(sky_board[0])):
                print(sky_board[row][col], end='', flush=True)
            print('\n', flush=True)
            
def main():
    print("Test Message: ")
    sky = Sky("test.txt", 100000, 14, 12)
    sky.parse_input()
    assert len(sky.stars) == 30, "test failed, should be 31"
    sky.message_in_the_sky()

    # print("Main input: ")
    # sky = Sky("input.txt", 100000, 66, 14)
    # sky.parse_input()
    # assert len(sky.stars) == 336, "test failed, should be 335"
    # sky.message_in_the_sky()

    print("Challenge input: ")
    sky = Sky("input_challenge.txt", 100000, 100, 11    )
    sky.parse_input()
    sky.message_in_the_sky()

if __name__ == '__main__':
    main()
