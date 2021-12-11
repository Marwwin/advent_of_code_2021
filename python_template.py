import sys
sys.path.append('../lib')


flatten = lambda x: [subl 
                        for l in x
                        for subl in l]

def open_file(filename: str)-> list[str]:
    with open(filename) as f:
        return(f.readlines())

def open_as_numerical_matrix(filename: str) -> list[str]:
    input_list = open_file(filename)
    matrix = [[int(n) for n in line.strip()] for line in input_list]
    return matrix

def get_neighbours_in_matrix(matrix: list[list[int]],pos: tuple[int,int],diagonals: bool=True)-> dict[tuple[int,int],int]:
    neighbours = {}
    (x,y) = pos
    if x != 0:
        neighbours[(x-1,y)] = matrix[x-1][y]
    if x != len(matrix)-1:
        neighbours[(x+1,y)] = matrix[x+1][y]    
    if y != 0:
        neighbours[(x,y-1)] = matrix[x][y-1]
    if y != len(matrix[0])-1:
        neighbours[(x,y+1)] = matrix[x][y+1]
    if diagonals:
        if x != 0 and y != 0:
            neighbours[(x-1,y-1)] = matrix[x-1][y-1] 
        if x != len(matrix)-1 and y != len(matrix[0])-1:  
            neighbours[(x+1,y+1)] = matrix[x+1][y+1]
        if x != len(matrix)-1 and y != 0:  
            neighbours[(x+1,y-1)] = matrix[x+1][y-1]
        if x != 0 and y != len(matrix[0])-1:  
            neighbours[(x-1,y+1)] = matrix[x-1][y+1] 
    return neighbours
