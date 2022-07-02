import * as util from "../utils/utils";
import { countIncreases, isIncrease, slidingWindow } from "./day1";

describe("day1", () => {
  let inputText: string[];

  test("Open input.txt file", () => {
    inputText = util.getInput("2021", "01");
    expect(inputText.length).toBe(2001);
  });
  test("Convert elements in input list into numbers", () => {
    const num: number[] = util.inputToNumbers(inputText);
    num.forEach((e) => expect(typeof e === "number"));
  });
  test("if number B is larger than A return true", () => {
    expect(isIncrease(1, 2) === true);
    expect(isIncrease(2, 1) === false);
  });
  test("Given a list of number count the number of increases", () => {
    expect(countIncreases([1, 2, 3, 4]) === 3);
    expect(
      countIncreases([
        199, 200, 208, 210, 200, 207, 240, 269, 260, 263,
      ]) === 7
    );
  });
  test("Create three-measurement sliding window", () => {
    expect(slidingWindow([1, 2, 3, 4],3) === [6, 9]);
    expect(
      slidingWindow([199, 200, 208, 210, 200, 207, 240, 269, 260, 263],3) ===
        [607, 618, 618, 617, 647, 716, 769, 792]
    );
  });
  test("Count increases of sliding window", () => {
    expect(
      countIncreases(
        slidingWindow([199, 200, 208, 210, 200, 207, 240, 269, 260, 263],3)
      ) === 5
    );
  });
  test("Solve Day 1", () => {
    console.log(
      "Day1 Part1",
      countIncreases(util.inputToNumbers(inputText))
    );
    console.log(
      "Day1 Part2",
      countIncreases(slidingWindow(util.inputToNumbers(inputText),3))
    );
  });
  console.log("over");
});
