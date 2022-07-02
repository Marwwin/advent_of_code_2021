const countIncreases = (input: number[]) => {
  let count = 0;
  for (let i = 1; i < input.length; i++) {
    if (isIncrease(input[i - 1], input[i])) count++;
  }
  return count;
};

const isIncrease = (a: number, b: number) => {
  return a < b;
};

const slidingWindow = (input: number[], size: number): number[] => {
  const sliding: number[] = [];
  for (let i = size - 1; i < input.length; i++) {
    const num = [...Array(size).keys()].reduce(
      (acc, index) => acc + input[i - index]
    );
    sliding.push(num);
  }
  return sliding;
};
export { isIncrease, countIncreases, slidingWindow };
