import * as utils from "../utils/utils";
import { solveDay5, addLine, parseLine } from "./day5";

describe("day5 part1", () => {

  test("given a line add 1 for each square to seafloor", () => {
    let seafloor = {};
    seafloor = addLine("0,0 -> 0,2", seafloor);
    const seafloorResult:{ [key: string]: number } = {};
    seafloorResult['0_0'] = 1;
    seafloorResult['0_1'] = 1;
    seafloorResult['0_2'] = 1;
    expect(seafloor).toEqual(seafloorResult);
  });

  test("parseLine should separate start from end", () => {
    expect(parseLine("0,0 -> 0,4")).toEqual([[0,0],[0,1],[0,2],[0,3],[0,4]]);
    expect(parseLine("0,0 -> 4,0")).toEqual([[0,0],[1,0],[2,0],[3,0],[4,0]]);
    expect(parseLine("9,4 -> 3,4")).toEqual([[3,4],[4,4],[5,4],[6,4],[7,4],[8,4],[9,4]]);


  });

  test("Count all numbers on seafloor larger than 2",() =>{
    const inputText = utils.getInput("2021", "05", "test_data.txt");
    expect(solveDay5(inputText)).toBe(5)
  })
  test("Count all numbers on seafloor larger than 2",() =>{
    const inputText = utils.getInput("2021", "05");
    expect(solveDay5(inputText)).toBe(5147)
  })
});
