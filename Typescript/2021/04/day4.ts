export class Bingo {
  #boards: Board[];
  #drawnNumbers: number[];
  #currentNumberIndex: number;
  constructor(inputData: string[]) {
    this.#drawnNumbers = inputData[0].split(",").map((e) => parseInt(e));
    this.#boards = this.parseBoards(inputData);
    this.#currentNumberIndex = 0;
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

  play(): number {
    const currentNumber = this.#drawnNumbers[this.#currentNumberIndex++];
    for (const board of this.#boards) {
      board.checkNumber(currentNumber);
    }
    return currentNumber;
  }

  currentNumber() {
    return this.#drawnNumbers[this.#currentNumberIndex];
  }

  get drawnNumbers() {
    return this.#drawnNumbers;
  }
  get boards() {
    return this.#boards;
  }
}

export class Board {
  #numbers: number[];
  #board: number[][];
  #hits: number[];
  constructor(listOfNumbers: number[][]) {
    this.#board = listOfNumbers;
    this.#numbers = listOfNumbers.flat(2);
    this.#hits = [];
  }

  checkNumber(n: number) {
    if (this.#numbers.some((e) => e === n)) {
      this.#hits.push(n);
    }
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
