import * as utils from "../utils/utils";
import { createSeafloor, addLine, parseLine } from "./day5";

describe("day5 part1", () => {
  test("create seafloor of size n*n", () => {
    const seafloor: { [key: string]: number } = {};
    seafloor['0_0'] = 0;
    seafloor['0_1'] = 0;
    seafloor['1_0'] = 0;
    seafloor['1_1'] = 0;

    expect(createSeafloor(2)).toStrictEqual(seafloor);
  });
  test("given a line add 1 for each square to seafloor", () => {
    let seafloor = createSeafloor(3);
    seafloor = addLine("0,0 -> 2,2", seafloor);
    const seafloorResult:{ [key: string]: number } = {};
    seafloorResult['0_0'] = 1;
    seafloorResult['0_1'] = 1;
    seafloorResult['0_2'] = 1;
    seafloorResult['1_0'] = 0;
    seafloorResult['1_1'] = 0;
    seafloorResult['1_2'] = 0;
    seafloorResult['2_0'] = 0;
    seafloorResult['2_1'] = 0;
    seafloorResult['2_2'] = 0;
    expect(seafloor).toEqual(seafloorResult);
  });

  test("parseLine should separate start from end", () => {
  //  expect(parseLine("0,0 -> 4,4")).toEqual({start:{x:0,y:0}, end:{x:4,y:4}});
    expect(parseLine("0,0 -> 0,4")).toEqual([[0,0],[0,1],[0,2],[0,3],[0,4]]);

  });
});
