#!/usr/bin/env python
import sys
from functools import reduce 

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

def maxChar(dict):
    maxChar = ""
    maxFreq = 0

    for (k, v) in dict.items():
        if v > maxFreq:
            maxFreq = v
            maxChar = k
        
    return maxChar

def maxChar_with_reduce(dict):
    return reduce(lambda dict_item, seq: dict_item if dict_item[1] > seq[1] else seq, dict.items())[0]

part1_decoded_pass = ""

for col in range(0, len(input[0].strip())):
    dict = {}
    for row in range(0, len(input)):
        element = input[row][col]

        if element in dict:
            dict[element] += 1
        else:
            dict[element] = 0
    
    max_char = maxChar_with_reduce(dict)

    part1_decoded_pass += str(max_char)

print("Final password: {}".format(part1_decoded_pass))