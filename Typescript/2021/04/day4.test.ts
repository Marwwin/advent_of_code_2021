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
    expect(bingo.play()).toBe(7);
    const boards = bingo.boards
    for (const board of boards){
        console.log(board.hits);
    }
    expect(bingo.play()).toBe(4);
  });
});
