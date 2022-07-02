import * as util from "../utils/utils";
import { Submarine } from "./day2_part1";
import { Submarine as Submarine2 } from "./day2_part2";


describe("day2 part1", () => {
  test("Open input.txt file", () => {
    const inputText = util.getInput("2021", "02", "test1.txt");
    expect(inputText.length).toBe(6);
  });
  test("Create a submarine that has a position and depth", () => {
    const submarine = new Submarine();
    expect(submarine.position).toBe(0);
    expect(submarine.depth).toBe(0);
  });
  test("A forward command should increase the submarines position", () => {
    const submarine = new Submarine();
    submarine.forward(1);
    expect(submarine.position).toBe(1);
  });
  test("A down command should increase the submarines depth", () => {
    const submarine = new Submarine();
    submarine.down(1);
    expect(submarine.depth).toBe(1);
  });
  test("A up command should decrease the submarines depth", () => {
    const submarine = new Submarine();
    submarine.down(1);
    submarine.up(1);
    expect(submarine.depth).toBe(0);
  });
  test("A list of commands should move the submarine correctly", () => {
    const inputText = util.getInput("2021", "02", "test1.txt");
    const submarine = new Submarine();
    submarine.takeOrders(inputText);
    expect(submarine.position).toBe(15);
    expect(submarine.depth).toBe(10);
  });
  test("Solve part 1", () => {
    const inputText = util.getInput("2021", "02");
    const submarine = new Submarine();
    submarine.takeOrders(inputText);
    expect(submarine.position * submarine.depth).toBe(1670340);
    console.log(submarine.position * submarine.depth);
  });
});
describe("day2 part2", () => {
    test("forward should move of the submarine according to its aim",()=>{
        const submarine = new Submarine2()
        submarine.down(10);
        expect(submarine.aim).toBe(10);
        submarine.up(5);
        expect(submarine.aim).toBe(5);
        submarine.forward(5);
        expect(submarine.position).toBe(5);
        expect(submarine.depth).toBe(25);
    })  
    test("A list of commands should move the submarine correctly", () => {
        const inputText = util.getInput("2021", "02", "test1.txt");
        const submarine = new Submarine2();
        submarine.takeOrders(inputText);
        expect(submarine.position).toBe(15);
        expect(submarine.depth).toBe(60);
        expect(submarine.position * submarine.depth).toBe(900);
      });

      test("Solve part 2", () => {
        const inputText = util.getInput("2021", "02");
        const submarine = new Submarine2();
        submarine.takeOrders(inputText);
        expect(submarine.position * submarine.depth).toBe(1954293920);
      });
});