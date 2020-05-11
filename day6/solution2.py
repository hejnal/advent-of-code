#!/usr/bin/env python
import sys

def decrypt_msg(input):
    pass

# eedadn
# drvtee
# eandsr
# raavrd
# atevrs
# tsrnev
# sdttsa
# rasrtv
# nssdts
# ntnada
# svetve
# tesnvt
# vntsnd
# vrdear
# dvrsen
# enarar

#'aderatsrnna' -> 'a' maxChar

# it column, raw

# input file
with open("input.txt") as file:
    input = file.readlines()


print("Read input: {}".format(input))
print("First char: {}".format(input[0][1]))

def maxChar(dict):
    maxChar = ""
    maxFreq = 0

    for (k, v) in dict.items():
        if v > maxFreq:
            maxFreq = v
            maxChar = k
        
    return maxChar

def minChar(dict):
    minChar = ""
    minFreq = sys.maxsize

    for (k, v) in dict.items():
        if v < minFreq:
            minFreq = v
            minChar = k
        
    return minChar


part1_decoded_pass = ""
part2_decoded_pass = ""

for col in range(0, len(input[0].strip())):
    dict = {}
    for row in range(0, len(input)):
        element = input[row][col]

        if element in dict:
            dict[element] += 1
        else:
            dict[element] = 0
    
    print("Dictionary is: {}".format(dict))
    max_char = maxChar(dict)
    min_char = minChar(dict)

    part1_decoded_pass += str(max_char)
    part2_decoded_pass += str(min_char)


print("Final password: {}".format(part1_decoded_pass))
print("Final password 2: {}".format(part2_decoded_pass))