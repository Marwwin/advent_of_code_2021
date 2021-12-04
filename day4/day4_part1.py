# %%
import numpy as np

bingo = [line for line in open("day4.txt").readlines()]


def flatten(x): return [sub
                        for lst in x
                        for sub in lst]


def get_drawn_numbers(inp):
    drawn_nums = inp[0].split("\n")[0].split(",")
    drawn_nums = [int(num) for num in drawn_nums]
    return drawn_nums


def get_bingo_boards(inp):
    boards = []
    board = []
    for line in inp[2:]:
        if line != "\n":
            line = line.split("\n")[0].split(" ")
            line = [int(num) for num in line if num != ""]
            board.append(line)
        else:
            boards.append(board)
            board = []
    return boards


def is_line_a_winner(line, drawn_nums):
    return all(num in drawn_nums for num in line)


def is_winning_board(board, drawn_numbers):
    np_board = np.array(board)
    for i in range(len(board)):
        if is_line_a_winner(np_board[:, i], drawn_numbers):
            return board
        if is_line_a_winner(np_board[i], drawn_numbers):
            return board


def get_winning_board():
    input_nums = get_drawn_numbers(bingo)
    boards = get_bingo_boards(bingo)
    drawn_numbers = []
    for n in input_nums:
        drawn_numbers.append(n)
        for board in boards:
            if is_winning_board(board, drawn_numbers):
                return board, drawn_numbers


def get_last_winning_board():
    input_nums = get_drawn_numbers(bingo)
    boards = get_bingo_boards(bingo)
    last_winning_board = []
    drawn_numbers = []
    for n in input_nums:
        drawn_numbers.append(n)
        boards = remove_winning_boards(boards, drawn_numbers)
        if len(boards) == 1:
            last_winning_board = boards[0]
        if len(boards) == 0:
            return last_winning_board, drawn_numbers


def remove_winning_boards(boards, drawn_numbers):
    return [board for board in boards if not is_winning_board(board, drawn_numbers)]


def print_answer(board, drawn_numbers):
    print(sum(num for num in flatten(board) if num not in drawn_numbers)
          * drawn_numbers[-1])


winner, drawn_numbers = get_winning_board()
print("Part 1:")
print_answer(winner, drawn_numbers)
winner, drawn_numbers = get_last_winning_board()
print("Part 2:")
print_answer(winner, drawn_numbers)
