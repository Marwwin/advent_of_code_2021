import { Matrix } from "../utils/utils";

export class Bingo {
  #boards: Board[];
  #drawnNumbers: number[];
  #currentNumberIndex: number;
  #boardsWon:number;
  constructor(inputData: string[]) {
    this.#drawnNumbers = inputData[0].split(",").map((e) => parseInt(e));
    this.#boards = this.parseBoards(inputData);
    this.#currentNumberIndex = 0;
    this.#boardsWon = 0;
  }

  parseBoards(inputData: string[]) {
    const rawData = inputData.slice(2);
    const boards: Board[] = [];
    let tempBoard = [];
    for (const line of rawData) {
      if (line === "") {
        boards.push(new Board(tempBoard));
        tempBoard = [];
      } else {
        const numLine = line
          .split(" ")
          .filter((e) => e !== "")
          .map((e) => parseInt(e));
        tempBoard.push(numLine);
      }
    }
    boards.push(new Board(tempBoard));
    return boards;
  }

  play() {
    const currentNumber = this.#drawnNumbers[this.#currentNumberIndex++];
    const boardsLeft = this.#boards.filter(board => !board.won)
    for (const board of boardsLeft) {
      board.checkNumber(currentNumber);
    }
    return boardsLeft.filter(board => board.won)
  }



  currentNumber() {
    return this.#drawnNumbers[this.#currentNumberIndex];
  }
  currentNumberI() {
    return this.#currentNumberIndex
  }

  get drawnNumbers() {
    return this.#drawnNumbers;
  }
  get boards() {
    return this.#boards;
  }
  get boardsWon(){
    return this.#boardsWon;
  }
}

export class Board {
  #numbers: number[];
  #board: number[][];
  #hits: number[];
  #won:boolean;
  constructor(listOfNumbers: number[][]) {
    this.#board = listOfNumbers;
    this.#numbers = listOfNumbers.flat(2);
    this.#hits = [];
    this.#won = false;
  }

  checkNumber(n: number) {
    if (this.#numbers.some((e) => e === n)) {
      this.#hits.push(n);
    }
    if (this.isWin()) {
      this.#won = true;
    }
  }

  winningScore(){
    return this.getSumOfNonHits() * this.#hits[this.#hits.length -1 ];
  }

  private isWin() {
    return (
      Matrix.isRow(this.#hits, this.#board) ||
      Matrix.isColumn(this.#hits, this.#board) 
      //Matrix.isDiagonal(this.#hits, this.#board)
    );
  }

  getSumOfNonHits(): number {
    return this.#numbers
      .filter((n) => !this.#hits.includes(n))
      .reduce((tot, num) => tot + num);
  }

  get won():boolean{
    return this.#won;
  }
  get numbers(): number[] {
    return this.#numbers;
  }
  get board(): number[][] {
    return this.#board;
  }
  get hits(): number[] {
    return this.#hits;
  }
}
