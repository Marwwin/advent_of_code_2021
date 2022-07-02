import * as fs from "fs";

export const getInput = (year: string, day: string, input:string = 'input.txt'): string[] => {
  return fs.readFileSync(`../${year}/${day}/${input}`,"utf-8").split("\n");
};

export const inputToNumbers = (input: string[]): number[] => {
  return input.map((e: string) => parseInt(e));
};
