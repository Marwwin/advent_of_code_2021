import * as util from "../utils/utils";

describe("day3 part1", () => {
  test("Open input.txt file", () => {
    const inputText = util.getInput("2021", "02", "test_data.txt");
    expect(inputText.length).toBe(12);
  });
});
