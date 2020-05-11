#!/usr/bin/env python

test_input = ["ULL", "RRDDD", "LURDL", "UUUUD"]

# can you see it?

keypad = [
   {},
   {'r': 2, 'l': 1, 'u': 1, 'd': 4},
   {'r': 3, 'l': 1, 'u': 2, 'd': 5},
   {'r': 3, 'l': 2, 'u': 3, 'd': 6},
   {'r': 5, 'l': 4, 'u': 1, 'd': 7},
   {'r': 6, 'l': 4, 'u': 2, 'd': 8},
   {'r': 6, 'l': 5, 'u': 3, 'd': 9},
   {'r': 8, 'l': 7, 'u': 4, 'd': 7},
   {'r': 9, 'l': 7, 'u': 5, 'd': 8},
   {'r': 9, 'l': 8, 'u': 6, 'd': 9}
]

def main():
   current_index = 5
   final_code = ''

   with open('input.txt', 'r') as input:
      for line in input:
         for char in line:
            if char == '\n':
                 continue

            current_index = keypad[current_index][char.lower()]
         final_code = final_code + str(current_index)
   print(final_code)

main()