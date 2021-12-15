#%%

def solve_day13():
    coords, folds = get_coords_and_folds()
    for fold in folds:
        axis, n = fold.split("=")
        if "y" in axis:
            coords = fold_y(coords,int(n))
            print(len(set(coords)))
        if "x" in axis:
            coords = fold_x(coords,int(n))
            print(len(set(coords)))
    matrix = generate_matrix(coords)
    print_matrix(matrix)
    
def open_file(filename: str)-> list[str]:
    with open(filename) as f:
        return(f.readlines())

def get_coords_and_folds():
    coords = []
    folds = []
    for x in [x.strip() for x in open_file("day14.txt")]:
        if "fold" in x:
            folds.append(x)
        elif "," in x:
            coords.append([int(n) for n in x.split(",")])
    return coords, folds

def get_max_value(coords,xy=0):
    return max([x[xy] for x in coords])

def generate_matrix(coords):
    max_x = get_max_value(coords,0)
    max_y = get_max_value(coords,1)
    matrix = []
    for y in range(max_y+1):
        row = []
        for x in range(max_x+1):
            if (x,y) in coords:
                row.append(u"\u25AE")
            else:
                row.append(" ")
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        for col in row:
            print(col,end="")
        print()

def fold_x(coords,n):
    return [(coord[0],coord[1]) if coord[0]<=n else (abs(coord[0]-n*2),coord[1]) for coord in coords]
def fold_y(coords,n):
    return [(coord[0],coord[1]) if coord[1]<=n else (coord[0],abs(coord[1]-n*2)) for coord in coords]

solve_day13()