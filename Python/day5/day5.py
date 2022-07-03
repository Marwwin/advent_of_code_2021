#%%
from typing import Counter
flatten = lambda x: [sub
                    for lst in x
                    for sub in lst]
import sys
sys.path.append('../lib')
import advent_of_code


def create_points(lines):
    vents = []
    for line in lines:
        raw_text = line.split("\n")[0].split(" -> ")
        a = raw_text[0].split(",")
        b = raw_text[1].split(",")
        vents.append([a,b])
    return vents

def get_vertical_and_horisontal(vents):
    return [vent for vent in vents if line_vertical_or_horisontal(vent)]

def get_diagonals(vents):
    return [vent for vent in vents if abs(int(vent[0][0]) - int(vent[1][0])) == abs(int(vent[0][1]) - int(vent[1][1]))]


def line_vertical_or_horisontal(line):
    return True if line[0][0] == line[1][0] or line[0][1] == line[1][1] else False

def create_horisontal_vertical_lines(vents):
    lines = []
    for points in vents:
        line = []
        a = points[0]
        b = points[1]
        if a[0] == b[0]:
            small = min([int(a[1]),int(b[1])])
            large = max([int(a[1]),int(b[1])])
            for i in range(small,large+1):
                line.append((int(a[0]),i))
        else:
            small = min([int(a[0]),int(b[0])])
            large = max([int(a[0]),int(b[0])])
            for i in range(small,large+1):
                line.append((i,int(a[1])))
        lines.append(line)
    return lines

def create_diagonals(vents):
    lines = []
    for points in vents:
        a = points[0]
        b = points[1] 

        if int(a[0]) < int(b[0]):
            lines.append(diagonal(a,b))
        else:
            lines.append(diagonal(b,a))
    return lines
def diagonal(a,b):
    line = []

    start_x = int(a[0])
    stop_x = int(b[0])
    start_y = int(a[1])
    stop_y = int(b[1])
    for i in range(0,stop_x-start_x+1):
        if stop_y > start_y:
            line.append((start_x+i,start_y+i))
        else:
            line.append((start_x+i,start_y-i))
    return line

def solve_part1():
    input_data = advent_of_code.open_file("day5.txt")
    vents = create_points(input_data)
    vents = get_vertical_and_horisontal(vents)
    lines = create_horisontal_vertical_lines(vents)
    print(len([x  for x in Counter(flatten(lines)).items() if x[1]>= 2]))

def solve_part2():
    input_data = advent_of_code.open_file("/home/marwwin/Documents/Personal/advent_of_code/day5/day5.txt")
    vents = create_points(input_data)
    lines = get_vertical_and_horisontal(vents)
    lines = create_horisontal_vertical_lines(lines)
    diagonals = create_diagonals(get_diagonals(vents))
    lines.extend(diagonals)
    print(len([x  for x in Counter(flatten(lines)).items() if x[1]>= 2]))
    return lines




lines = solve_part2()
#print(max(lines))
#for y in range(10):
#    for x in range(10):
#        ch = Counter(flatten(lines))[(x,y)]
#        if ch == 0:
#            print(".",end="")
#        else:
#            print(ch,end="")
#    print()

#%%
abs(-5)