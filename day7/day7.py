#%%
import sys
sys.path.append('../lib')

import advent_of_code

input_list = advent_of_code.open_file("day7.txt")

def create_crabs_list(input_list):
    crabs = parse_crabs(input_list)
    crabs_list = {x:0 for x in range(0,max(crabs)+1)}
    for crab in crabs:
        crabs_list[crab] += 1
    return crabs_list

def parse_crabs(input_list):
    crabs = [int(n) for n in input_list[0].split(",")]
    return crabs

def find_optimal_position_part1(crabs_list):
    max_value = max(crabs_list.keys())
    optimal_solution = 1000000
    for x in range(max_value+1):
        solution = 0
        for crab_i in crabs_list.keys():
            solution += crabs_list[crab_i] * abs(int(x)-int(crab_i))
        if solution < optimal_solution:
            optimal_solution = solution

    return optimal_solution

def find_optimal_position_part2(crabs_list):
    max_value = max(crabs_list.keys())
    optimal_solution = 10000000000
    for x in range(max_value+1):
        solution = 0
        for crab_i in crabs_list.keys():
            solution += crabs_list[crab_i] * sum(range(1,abs(int(x)-int(crab_i))+1))
        if solution < optimal_solution:
            optimal_solution = solution

    return optimal_solution

crabs_list = create_crabs_list(input_list)    
find_optimal_position_part1(crabs_list)
find_optimal_position_part2(crabs_list)


