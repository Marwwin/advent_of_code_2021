#%%
import sys
sys.path.append('../')
import advent_of_code

input_list = advent_of_code.open_file("input.txt")

len([x for x in zip(input_list[:-1],input_list[1:]) if int(x[0]) < int(x[1])])