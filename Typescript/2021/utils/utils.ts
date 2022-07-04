import * as fs from "fs";

export const getInput = (
  year: string,
  day: string,
  input: string = "input.txt"
): string[] => {
  return fs.readFileSync(`../${year}/${day}/${input}`, "utf-8").split("\n");
};

export const inputToNumbers = (input: string[]): number[] => {
  return input.map((e: string) => parseInt(e));
};

export abstract class Matrix {
  public static isRow(numbers: number[], matrix: number[][]) {
    return matrix.some((row) => row.every((n) => numbers.includes(n)));
  }
  public static isColumn(numbers: number[], matrix: number[][]) {
    const flippedMatrix = this.flipMatrix(matrix);
    return flippedMatrix.some((row) => row.every((n) => numbers.includes(n)));
  }
  public static flipMatrix(matrix: number[][]) {
    return matrix.map((row, i) => row.map((_, j) => matrix[j][i]));
  }
  public static isDiagonal(numbers: number[], matrix: number[][]) {
    const diagonals = this.extractDiagonals(matrix);
    return this.isRow(numbers, diagonals);
  }

  private static extractDiagonals(matrix: number[][]) {
    const lengthOfRow = matrix[0].length;
    const topLeft = [];
    const bottomLeft = [];
    for (let i = 0; i < lengthOfRow; i++) {
      topLeft.push(matrix[i][i]);
      const invertedI = lengthOfRow - i - 1
      bottomLeft.push(matrix[invertedI][i]);
    }
    return [topLeft, bottomLeft];
  }
}
