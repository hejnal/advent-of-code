#!/usr/bin/env python

def calculate_distance(input):
    angle=270

    horizontal=0
    vertical=0
    total_distance = 0
    
    for d in input:
        direction = d[0]
        distance = int(d[1:])

        print('I read direction: {}, and distance: {}'.format(direction, distance))
        
        print('Current angle: {}'.format(angle))
        
        if direction == 'R':
            angle = (angle + 90) % 360
        elif direction == 'L':
            angle -= 90
            if angle < 0:
                angle += 360

        if angle == 0:
            horizontal += distance
        elif angle == 90:
            vertical -= distance
        elif angle == 180:
            horizontal -= distance
        elif angle == 270:
            vertical += distance

        print('New angle: {}'.format(angle))


    total_distance = abs(horizontal) + abs(vertical)
    print('Total distance is: {}'.format(total_distance))
    
    return total_distance

def calculate_distance2(input):
    print('***********************************************************')
    angle=270

    horizontal=0
    vertical=0
    total_distance = 0

    visited_spots = [(0, 0)]
    
    for d in input:
        direction = d[0]
        distance = int(d[1:])

        print('I read direction: {}, and distance: {}'.format(direction, distance))
        
        print('Current angle: {}'.format(angle))

        if direction == 'R':
            angle = (angle + 90) % 360
        elif direction == 'L':
            angle -= 90
            if angle < 0:
                angle += 360

        print('New angle: {}'.format(angle))

        if angle == 0:
            for i in range(horizontal + 1, horizontal + distance + 1):
                
                if (i, vertical) in visited_spots:
                    horizontal = i
                    
                    print('Second time visiting spot: ({}, {})'.format(horizontal, vertical))
                    total_distance = abs(horizontal) + abs(vertical)

                    return total_distance
                    
                else:
                    print('Adding ({}, {}) to the list.'.format(i, vertical))
                    visited_spots.append((i, vertical))
            
            horizontal += distance
        elif angle == 90:
            for i in range(vertical - 1, vertical - distance - 1, -1):
                
                if (horizontal, i) in visited_spots:
                    vertical = i
                    print('Second time visiting spot: ({}, {})'.format(horizontal, vertical))
                    total_distance = abs(horizontal) + abs(vertical)

                    return total_distance
                    
                else:
                    print('Adding ({}, {}) to the list.'.format(horizontal, i))
                    visited_spots.append((horizontal, i))

            vertical -= distance
        elif angle == 180:
            for i in range(horizontal - 1, horizontal - distance - 1, -1):
                
                if (i, vertical) in visited_spots:
                    horizontal = i

                    print('Second time visiting spot: ({}, {})'.format(horizontal, vertical))
                    total_distance = abs(horizontal) + abs(vertical)

                    return total_distance
                else:
                    print('Adding ({}, {}) to the list.'.format(i, vertical))
                    visited_spots.append((i, vertical))

            horizontal -= distance
        elif angle == 270:
            for i in range(vertical + 1, vertical + distance + 1):
                
                if (horizontal, i) in visited_spots:
                    vertical = i

                    print('Second time visiting spot: ({}, {})'.format(horizontal, vertical))
                    total_distance = abs(horizontal) + abs(vertical)

                    return total_distance
                else:
                    print('Adding ({}, {}) to the list.'.format(horizontal, i))
                    visited_spots.append((horizontal, i))

            vertical += distance

        
        print('Current distance: x: {}, y: {}'.format(horizontal, vertical))


    total_distance = abs(horizontal) + abs(vertical)
    print('Total distance is: {}'.format(total_distance))
    print('Visited spots are: {}'.format(visited_spots))
    
    return total_distance


input = ['R2', 'L3']
distance = calculate_distance(input)
assert distance == 5, 'distance should be 5'

input = ['R2', 'R2', 'R2']
distance = calculate_distance(input)
assert distance == 2, 'distance should be 2'

input = ['R5', 'L5', 'R5', 'R3']
distance = calculate_distance(input)
assert distance == 12, 'distance should be 12'

input = ['R8', 'R4', 'R4', 'R8']
distance = calculate_distance2(input)
assert distance == 4, 'distance should be 12'

with open('input.txt') as f:
    line = f.readline()

    while line:
        print(line)
        input = map(str.strip, line.split(','))
        
        print(input)
        distance = calculate_distance2(input)
        
        print('Total distance: {}'.format(distance))
        line = f.readline()
