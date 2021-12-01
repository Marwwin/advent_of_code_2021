#%%
import sys
sys.path.append('../')
import advent_of_code

input_list = advent_of_code.open_file("input.txt")

def count_increase(input_list):
    nums = [int(l) for l in input_list]
    counter = 0
    prev = []
    for i in range(len(nums)-2):
        curr = [nums[i],nums[i+1],nums[i+2]]
        if not prev:
            prev = curr
        elif sum(curr) > sum(prev):
            counter += 1
        prev = curr
    return counter

count_increase(input_list)
