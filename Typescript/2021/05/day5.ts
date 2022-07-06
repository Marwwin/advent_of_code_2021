const solveDay5 = (input:string[]) => {
  const seafloor = createSeafloor
}

const createSeafloor = (size: number): { [key: string]: number } => {
  const seafloor: { [key: string]: number } = {};
  for (let x: number = 0; x < size; x++) {
    for (let y = 0; y < size; y++) {
      seafloor[`${x}_${y}`] = 0;
    }
  }
  return seafloor;
};

const addLine = (lineString: string, seafloor:  { [key: string]: number }) => {
  const line = parseLine(lineString);
  line.forEach(([x, y]) => {
    const prev = seafloor[`${x}_${y}`];
    seafloor[`${x}_${y}`] = prev + 1;
  });
  return seafloor;
};

const parseLine = (line: string) => {
  const [start, end] = line.split(" -> ");
  let [startx, starty] = start.split(",").map((e) => parseInt(e));
  const [endx, endy] = end.split(",").map((e) => parseInt(e));
  const result = [];
  for (startx; startx <= endx; startx++) {
    for (starty; starty <= endy; starty++) {
      result.push([startx, starty]);
    }
  }
  return result;
};

export { createSeafloor, addLine, parseLine };
