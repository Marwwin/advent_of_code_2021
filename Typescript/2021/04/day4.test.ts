import * as util from "../utils/utils";
import { Bingo, Board } from "./day4";

describe("day4", () => {
  test("Open input.txt file", () => {
    const inputText = util.getInput("2021", "04", "test_data.txt");
    expect(inputText.length).toBe(19);
  });
  test("Bingo game is instantiated", () => {
    const inputText = util.getInput("2021", "04", "test_data.txt");
    const bingo = new Bingo(inputText);
    expect(bingo.drawnNumbers).toHaveLength(27);
    expect(bingo.boards).toHaveLength(3);
  });
  test("Board is instantiated", () => {
    const boardData = [
      [3, 15, 0, 2, 22],
      [9, 18, 13, 17, 5],
      [19, 8, 7, 25, 23],
      [20, 11, 10, 24, 4],
      [14, 21, 16, 12, 6],
    ];
    const board = new Board(boardData);
    expect(board.numbers).toHaveLength(25);
    expect(board.board[0]).toHaveLength(5);
  });
  test("When the game progresses a new number should be drawn, If number on board it should be saved to board", () => {
    const inputText = util.getInput("2021", "04", "test_data.txt");
    const bingo = new Bingo(inputText);
    expect(bingo.play()).toStrictEqual({win:false,result:7});
    expect(bingo.play()).toStrictEqual({win:false,result:4});
  });
  const boardData = [
    [3, 15, 0, 2, 22],
    [9, 18, 13, 17, 5],
    [19, 8, 7, 25, 23],
    [20, 11, 10, 24, 4],
    [14, 21, 16, 12, 6],
  ];
  test("Given a square matrix and a list of numbers not matching any complete row return false", () => {
    const board = new Board(boardData);
    expect(util.Matrix.isRow([], board.board)).toBeFalsy();
    expect(util.Matrix.isRow([1, 2, 3], board.board)).toBeFalsy();
    expect(util.Matrix.isRow([1, 2, 3, 4, 5], board.board)).toBeFalsy();
  });
  test("Given a square matrix and a list of numbers return true if one row matches", () => {
    const board = new Board(boardData);
    expect(util.Matrix.isRow([0, 2, 3, 15, 22], board.board)).toBeTruthy();
  });
  test("Given a square matrix and a list of numbers return false if no full column matches", () => {
    const board = new Board(boardData);
    expect(util.Matrix.isColumn([], board.board)).toBeFalsy();
    expect(util.Matrix.isColumn([1, 2, 3], board.board)).toBeFalsy();
    expect(util.Matrix.isColumn([3, 9, 14, 19], board.board)).toBeFalsy();
  });
  test("Given a square matrix and a list of numbers return true if one column matches", () => {
    const board = new Board(boardData);
    expect(util.Matrix.isColumn([3, 9, 14, 19, 20], board.board)).toBeTruthy();
  });
  test("Given a square matrix and a list of numbers return false if no diagonal matches", () => {
    const board = new Board(boardData);
    expect(util.Matrix.isDiagonal([], board.board)).toBeFalsy();
    expect(util.Matrix.isDiagonal([1], board.board)).toBeFalsy();
    expect(util.Matrix.isDiagonal([1, 2, 3, 4, 5], board.board)).toBeFalsy();
  });
  test("Given a square matrix and a list of numbers return true if one diagonal matches", () => {
    const board = new Board(boardData);
    expect(util.Matrix.isDiagonal([3, 6, 7, 18, 24], board.board)).toBeTruthy();
    expect(
      util.Matrix.isDiagonal([7, 11, 14, 17, 22], board.board)
    ).toBeTruthy();
  });
  test("Play the game with test_data until one board wins", () => {
    const inputText = util.getInput("2021", "04", "test_data.txt");
    const bingo = new Bingo(inputText);
    let win = bingo.play();  
    while (!win.win) {
      win = bingo.play();
    }
    expect(win.result).toBe(4512);
  });
  test("Play the game until one board wins", () => {
    const inputText = util.getInput("2021", "04");
    const bingo = new Bingo(inputText);
    let win = bingo.play();  
    while (!win.win) {
      win = bingo.play();
    }
    expect(win.result).toBe(63552);
  });
  test("Play the game until the last board wins", () => {
    const inputText = util.getInput("2021", "04");
    const bingo = new Bingo(inputText);
    let win = bingo.play();  
    while (bingo.boardsWon < bingo.boards.length ) {
        console.log(bingo.boardsWon, bingo.boards.length, bingo.currentNumberI());
      win = bingo.play();
    }
    win = bingo.play();

    expect(win.result).toBe(9020);
  });
});
