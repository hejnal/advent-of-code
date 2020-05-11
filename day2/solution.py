#!/usr/bin/env python

def generate_pin(input):
    pinpad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # 1 2 3
    # 4 5 6
    # 7 8 9

    # ULL

    # xCoord, yCoord [0, 2]
    xCoord = 1
    yCoord = 1

    pin = ""

    for line in input:
        for d in line.strip():

            print("Read direction: {}".format(d))
            if d == 'L':
                yCoord = max(0, yCoord - 1)
            elif d == 'R':
                yCoord = min(2, yCoord + 1)
            elif d == 'U':
                xCoord = max(0, xCoord - 1)
            elif d == 'D':
                xCoord = min(2, xCoord + 1)

        print("xCoord: {}, yCoord: {}".format(xCoord, yCoord))
        pin = pin + str(pinpad[xCoord][yCoord])

    return pin

def generate_pin_phase2(input):
    pinpad = [['-1', '-1', '1', '-1', '-1'], ['-1', '2', '3', '4', '-1'], ['5', '6', '7', '8', '9'], ['-1', 'A', 'B', 'C', '-1'], ['-1', '-1', 'D', '-1', '-1']]

    #     1
    #   2 3 4
    # 5 6 7 8 9
    #   A B C
    #     D
    # ULL

    # xCoord, yCoord [0, 2]
    xCoord = 2
    yCoord = 0

    pin = ""

    for line in input:
        for d in line.strip():

            print("Read direction: {}".format(d))
            if d == 'L':
                if yCoord > 0 and pinpad[xCoord][yCoord - 1] != '-1':
                    yCoord -= 1
            elif d == 'R':
                if yCoord < 4 and pinpad[xCoord][yCoord + 1] != '-1':
                    yCoord += 1
            elif d == 'U':
                if xCoord > 0 and pinpad[xCoord - 1][yCoord] != '-1':
                    xCoord -= 1
            elif d == 'D':
                if xCoord < 4 and pinpad[xCoord + 1][yCoord] != '-1':
                    xCoord += 1

        print("xCoord: {}, yCoord: {}".format(xCoord, yCoord))
        pin = pin + str(pinpad[xCoord][yCoord])

    return pin

# quick test
input = ["ULL", "RRDDD","LURDL", "UUUUD"]
expected = '1985'
assert generate_pin(input) == expected, "Expected value is: {}".format(expected)

# input file
with open("input.txt") as file:
    input = file.readlines()

print("Read input: {}".format(input))
pin = generate_pin(input) 
print("Generated PIN value is: {}".format(pin))

# quick test
input = ["ULL", "RRDDD","LURDL", "UUUUD"]
expected = '5DB3'
assert generate_pin_phase2(input) == expected, "Expected value is: {}".format(expected)

# input file
with open("input.txt") as file:
    input = file.readlines()

print("Read input: {}".format(input))
pin = generate_pin_phase2(input) 
print("Generated PIN value is: {}".format(pin))
