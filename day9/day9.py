#%%
import sys
sys.path.append('../lib')

import advent_of_code
import numpy as np
import functools

input_list = advent_of_code.open_file("/home/makankko/Documents/advent_of_code_2021/day9/day9.txt")

input_list = [[int(n) for n in x.strip()] for x in input_list]

np_list = np.array(input_list)

def solve_part1(matrix):
  result = 0
  for i,line in enumerate(matrix):
    for j,num in enumerate(line):
      if is_low_point(matrix,(i,j)):
        result += 1+num
  return result

def find_neighbours(matrix,pos):
  neigbours = {"u":None,"d":None,"l":None,"r":None}
  if pos[1] != len(matrix[0])-1:
    neigbours["r"] = matrix[pos[0]][pos[1]+1]
  if pos[1] != 0:
    neigbours["l"] = matrix[pos[0]][pos[1]-1]
  if pos[0] != len(matrix)-1:
    neigbours["d"] = matrix[pos[0]+1][pos[1]]
  if pos[0] != 0:
    neigbours["u"] = matrix[pos[0]-1][pos[1]]
  return neigbours

def is_low_point(matrix,pos):
  neighbours = find_neighbours(matrix,pos)
  current = matrix[pos[0]][pos[1]]
  return all([x > current for x in neighbours.values() if x != None])

def matrix_at(matrix,pos):
  return matrix[pos[0]][pos[1]]

def solve_part2(matrix):
  basins = []
  for i,line in enumerate(matrix):
    for j,num in enumerate(line):
      if is_low_point(matrix,(i,j)):
        bas = find_basin(matrix,(i,j),[])
        basins.append(len(set(bas)))
        
  return sorted(basins)

def find_basin(matrix,pos,res):
  res.append(pos)
  neighbours = find_neighbours(matrix,pos)
  higer_points = [key for key in neighbours if neighbours[key] != None and neighbours[key] != 9 and neighbours[key] > matrix_at(matrix,pos)]
  for point in higer_points:
    if point == "l":
      res = find_basin(matrix,(pos[0],pos[1]-1),res)
    if point == "r":
      res = find_basin(matrix,(pos[0],pos[1]+1),res)
    if point == "d":
      res = find_basin(matrix,(pos[0]+1,pos[1]),res)
    if point == "u":
      res = find_basin(matrix,(pos[0]-1,pos[1]),res)
  return res

#bas = find_basin(np_list,(2,2))
#print(bas)
#print(len(set(bas)))
bas = solve_part2(np_list)
print(functools.reduce(lambda a,b: a*b,bas[-3:]))

