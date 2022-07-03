#%%
from typing import Counter
import numpy as np

lines = [[y for y in x.split("\n")[0]] for x in open("day3.txt").readlines()]

def get_most_common(lines,pos):
  counts = Counter(lines[:,pos])
  most_common = counts.most_common(2)
  if len(most_common) == 1:
    return most_common[0][0]
  if most_common[0][1] == most_common[1][1]:
    return "1"
  else:
    return counts.most_common(1)[0][0]

def get_least_common(lines,pos):
  counts = Counter(lines[:,pos])
  most_common = counts.most_common(2)
  if len(most_common) == 1:
    return most_common[0][0]
  if most_common[0][1] == most_common[1][1]:
    return "0"
  else:
    return counts.most_common(2)[1][0]

def get_lines(lines,pos,mc):
  return [line for line in lines if line[pos] == mc]


co2 = 0
oxy = 0

t = np.array(lines.copy())

for i in range(len(lines[0])):
  mc = get_most_common(t,i)
  t = np.array(get_lines(t,i,mc))
  if len(t) == 1:
    print(t)
    oxy = int("".join(t[0]),2)
    break
t = np.array(lines.copy())

for i in range(len(lines[0])):
  mc = get_least_common(t,i)
  t = np.array(get_lines(t,i,mc))
  if len(t) == 1:
    print(t)
    co2 = int("".join(t[0]),2)
    break

print(oxy*co2)


