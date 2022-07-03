import * as util from "../utils/utils";
import {
  flipBits,
  getPowerConsumption,
  mostCommonBitByIndex,
  listToMostCommonBit,
  numberWithMostCommonBits,
} from "./day3";

describe("day3 part1", () => {
  test("Open input.txt file", () => {
    const inputText = util.getInput("2021", "03", "test_data.txt");
    expect(inputText.length).toBe(12);
  });
  test("Find most common bit by index", () => {
    const inputText = util.getInput("2021", "03", "test_data.txt");
    expect(mostCommonBitByIndex(inputText, 0)).toBe(1);
    expect(mostCommonBitByIndex(inputText, 1)).toBe(0);

  });
  test("given a list of binary numbers return a binary number consisting of the most common bit of each index", () => {
    const inputText = util.getInput("2021", "03", "test_data.txt");
    expect(listToMostCommonBit(inputText)).toBe("10110");
  });
  test("Solve part1", () => {
    const inputText = util.getInput("2021", "03");
    const gamma = listToMostCommonBit(inputText);
    const epsilon = flipBits(gamma);
    expect(getPowerConsumption(gamma, epsilon)).toBe(1092896);
  });

  test("Given a list of binary numbers return the number consisting of most common bits", () => {
    const inputText = util.getInput("2021", "03", "test_data.txt");
    expect(numberWithMostCommonBits(inputText)).toBe("10111")
    expect(numberWithMostCommonBits(inputText, false)).toBe("01010")
  })
  test("solve part 2",() => {
    const inputText = util.getInput("2021", "03");
    const gamma = numberWithMostCommonBits(inputText);
    const epsilon = numberWithMostCommonBits(inputText,false);
    expect(getPowerConsumption(gamma, epsilon)).toBe(4672151);
  })

});
