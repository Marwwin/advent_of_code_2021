#%%

lines = [x for x in open("day3.txt").readlines()]

res = [0,0,0,0,0,0,0,0,0,0,0,0]
for line in lines:
  for i,bit in enumerate(line.strip("\n")):
    res[i] += int(bit)

gamma = [str(0) if b<0 else str(1) for b in [len(lines)/2-x for x in res]]
epsilon = [str(0) if b>0 else str(1) for b in [len(lines)/2-x for x in res]]

int("".join(gamma),2) * int("".join(epsilon),2)

