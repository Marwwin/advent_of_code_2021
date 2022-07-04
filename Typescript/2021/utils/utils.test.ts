import * as utils from "./utils";

describe("Utils matrix functions", () => {
  test("Given a matrix flip rows and columns", () => {
    const matrix = [
      [1, 2],
      [3, 4],
    ];
    expect(utils.Matrix.flipMatrix(matrix)).toEqual([
      [1, 3],
      [2, 4],
    ]);
  });
});
