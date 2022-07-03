# %%
import sys
sys.path.append('../lib')


def flatten(x): return [subl
                        for l in x
                        for subl in l]


def open_file(filename: str) -> list[str]:
    with open(filename) as f:
        return(f.readlines())


def open_as_numerical_matrix(filename: str) -> list[list[int]]:
    input_list = open_file(filename)
    matrix = [[int(n) for n in line.strip()] for line in input_list]
    return matrix


class DumboOctopus:
    def __init__(self, filename) -> None:
        self.matrix = open_as_numerical_matrix(filename)

    def solve(self) -> None:
        matrix = self.matrix.copy()
        flashes = 0
        i = 0
        while True:
            if self.are_all_flashing(matrix):
                print("All flashed:", i)
                break
            matrix = self.next_step(matrix)
            if self.is_over_10_in_matrix(matrix):
                new_flashes, matrix = self.flash(matrix)
                flashes += new_flashes
            if i == 100:
                print("Number of flashes at 100:", flashes)
            i += 1

    def next_step(self, matrix: list[list[int]]) -> list[list[int]]:
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                matrix[x][y] += 1
        return matrix

    def flash(self, matrix: list[list[int]]) -> tuple[int, list[list[int]]]:
        flashes = 0
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if matrix[x][y] >= 10:
                    flashes += 1
                    matrix[x][y] = 0
                    neighbours = self.get_neighbours_in_matrix(matrix, (x, y))
                    for (x, y) in neighbours:
                        if matrix[x][y] != 0:
                            matrix[x][y] += 1
        if self.is_over_10_in_matrix(matrix):
            new_flashes, matrix = self.flash(matrix)
            flashes += new_flashes
        return flashes, matrix

    def get_neighbours_in_matrix(self, matrix: list[list[int]], pos: tuple[int, int], diagonals: bool = True) -> dict[tuple[int, int], int]:
        neighbours = {}
        (x, y) = pos
        if x != 0:
            neighbours[(x-1, y)] = matrix[x-1][y]
        if x != len(matrix)-1:
            neighbours[(x+1, y)] = matrix[x+1][y]
        if y != 0:
            neighbours[(x, y-1)] = matrix[x][y-1]
        if y != len(matrix[0])-1:
            neighbours[(x, y+1)] = matrix[x][y+1]
        if diagonals:
            if x != 0 and y != 0:
                neighbours[(x-1, y-1)] = matrix[x-1][y-1]
            if x != len(matrix)-1 and y != len(matrix[0])-1:
                neighbours[(x+1, y+1)] = matrix[x+1][y+1]
            if x != len(matrix)-1 and y != 0:
                neighbours[(x+1, y-1)] = matrix[x+1][y-1]
            if x != 0 and y != len(matrix[0])-1:
                neighbours[(x-1, y+1)] = matrix[x-1][y+1]
        return neighbours

    def is_over_10_in_matrix(self, matrix: list[list[int]]) -> bool:
        return not all([n < 10 for n in flatten(matrix)])

    def are_all_flashing(self, matrix: list[list[int]]) -> bool:
        return True if all([n == 0 for n in flatten(matrix)]) else False

    def print_matrix(self, matrix: list[list[int]]) -> None:
        for m in matrix:
            print(m)
        print()


octopus = DumboOctopus("day11.txt")
octopus.solve()

# %%

#    match pos:
#        case (x,y) if x != 0 and y != 0 and x != len(matrix)-1 and y != len(matrix[0])-1:
#            neighbours["lu"] = matrix[x-1][y-1]
#            neighbours["u"] = matrix[x-1][y]
#            neighbours["ur"] = matrix[x-1][y+1]
#            neighbours["r"] = matrix[x][y+1]
#            neighbours["dr"] = matrix[x+1][y+1]
#            neighbours["d"] = matrix[x+1][y]
#            neighbours["dl"] = matrix[x+1][y-1]
#            neighbours["l"] = matrix[x][y-1]
#        case (0,0):
#            neighbours["r"] = matrix[0][1]
#            neighbours["dr"] = matrix[1][1]
#            neighbours["d"] = matrix[1][0]
#        case (x,y) if x == len(matrix)-1 and y == len(matrix)-1:
#            neighbours["l"] = matrix[x][y-1]
#            neighbours["lu"] = matrix[x-1][y-1]
#            neighbours["u"] = matrix[x-1][y]
#        case (x,y) if x == len(matrix)-1:
#            neighbours["lu"] = matrix[x-1][y-1]
#            neighbours["u"] = matrix[x-1][y]
#            neighbours["ur"] = matrix[x-1][y+1]
#            neighbours["r"] = matrix[x][y+1]
#            neighbours["l"] = matrix[x][y-1]
#        case (x,y) if y == len(matrix[0])-1:
#            neighbours["d"] = matrix[x+1][y]
#            neighbours["dl"] = matrix[x+1][y-1]
#            neighbours["l"] = matrix[x][y-1]
#            neighbours["lu"] = matrix[x-1][y-1]
#            neighbours["u"] = matrix[x-1][y]
#        case (0,y):
#            neighbours["r"] = matrix[0][y+1]
#            neighbours["dr"] = matrix[1][y+1]
#            neighbours["d"] = matrix[1][y]
#            neighbours["dl"] = matrix[1][y-1]
#            neighbours["l"] = matrix[0][y-1]
#        case (x,0):
#            neighbours["u"] = matrix[x-1][0]
#            neighbours["ur"] = matrix[x-1][1]
#            neighbours["r"] = matrix[x][1]
#            neighbours["dr"] = matrix[x+1][1]
#            neighbours["d"] = matrix[x+1][0]
#    return neighbours
