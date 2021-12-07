#%%
import sys
sys.path.append('../lib')

import advent_of_code

input_list = advent_of_code.open_file("day7.txt")

def create_crabs(input_list):
    parsed_list = parse_crabs(input_list)
    crabs = {x:0 for x in range(0,max(parsed_list)+1)}
    for num in parsed_list:
        crabs[num] += 1
    return crabs

def parse_crabs(input_list):
    crabs = [int(n) for n in input_list[0].split(",")]
    return crabs

def find_optimal_position(crabs,constant_burn=True):
    max_value = max(crabs.keys())
    optimal_solution = None
    for pos in range(max_value+1):
        solution = 0
        for crab_pos in crabs.keys():
            if constant_burn:
                solution += crabs[crab_pos] * abs(pos-crab_pos)
            else:
                solution += crabs[crab_pos] * sum(range(1,abs(pos-crab_pos)+1))
        if not optimal_solution or solution < optimal_solution:
            optimal_solution = solution
    return optimal_solution

crabs = create_crabs(input_list)    
print(find_optimal_position(crabs,True))
print(find_optimal_position(crabs,False))



