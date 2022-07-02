export class Submarine {
  #position: number;
  #depth: number;
  #aim: number;

  constructor() {
    this.#position = 0;
    this.#depth = 0;
    this.#aim = 0;
  }
  get position() {
    return this.#position;
  }
  get depth() {
    return this.#depth;
  }
  get aim() {
    return this.#aim;
  }
  takeOrders(listOfCommands: string[]) {
    listOfCommands.forEach((command) => {
      this.move(command);
    });
  }
  move(input: string) {
    const [command, n] = input.split(" ");
    switch (command) {
      case "forward":
        this.forward(parseInt(n));
        break;
      case "down":
        this.down(parseInt(n));
        break;
      case "up":
        this.up(parseInt(n));
        break;
    }
  }
  forward(n: number) {
    this.#position += n;
    this.#depth += this.#aim * n;
  }
  down(n: number) {
    this.#aim += n;
  }
  up(n: number) {
    this.#aim -= n;
  }
}
