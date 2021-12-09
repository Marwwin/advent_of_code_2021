#%%

import sys
from typing import Mapping
sys.path.append('../lib')
import re
import advent_of_code
flatten = lambda l: [subl
                    for list in l 
                    for subl in list]
input_list = advent_of_code.open_file("day8.txt")

def solve_part2(input_list):
  patterns, output = parse_input(input_list)
  mappings = extract_mappings(patterns)

  print_result(mappings,output)

def extract_mappings(patterns):
  mappings = []
  for i,pattern in enumerate(patterns):
    one = get_nums_of_length(pattern,2)[0]
    four = get_nums_of_length(pattern,4)[0]
    seven = get_nums_of_length(pattern,3)[0]
    eight = get_nums_of_length(pattern,7)[0]

    str_length_six = get_nums_of_length(pattern,6)
    str_length_five = get_nums_of_length(pattern,5)

    three = extract_number(str_length_five,seven,2)
    nine = extract_number(str_length_six,three,1)
    six = extract_number(str_length_six,one,5)
    two = extract_number([num for num in str_length_five if num != three],six,1)
    five = extract_number(str_length_five,six,0)
    zero = [num for num in str_length_six if num != nine and num != six ][0]


    mapping = {
      "".join(sorted(zero)):0,
      "".join(sorted(one)):1,
      "".join(sorted(two)):2,
      "".join(sorted(three)):3,
      "".join(sorted(four)):4,
      "".join(sorted(five)):5,
      "".join(sorted(six)):6,
      "".join(sorted(seven)):7,
      "".join(sorted(eight)):8,
      "".join(sorted(nine)):9
    }
    mappings.append(mapping)

  return mappings

def extract_number(patterns,b,target):
  for pattern in patterns:
    if len(str_minus(pattern,b)) == target:
      return pattern

def get_nums_of_length(patterns,n):
  return [pattern for pattern in patterns if len(pattern) == n]

def str_minus(a,b):
  return re.sub("["+b+"]","",a)

def parse_input(input_list):
  patterns = [pattern.split(" | ")[0].split(" ") for pattern in input_list]
  output = [pattern.split(" | ")[1].split("\n")[0].split(" ") for pattern in input_list]
  return patterns,output

def print_result(mappings,output):
  res = 0
  for i in range(len(output)):
    out = ["".join(sorted(x)) for x in output[i]]
    value = ""
    for o in out:
      value += str(mappings[i][o])  
    res += int(value)
  print(res)
solve_part2(input_list)

