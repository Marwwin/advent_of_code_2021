interface OceanFloor {
  [key: string]: number;
}

const solveDay5 = (input: string[]) => {
  let seafloor: OceanFloor = {};
  for (let line of input) {
    seafloor = addLine(line, seafloor);
  }
  return Object.values(seafloor)
    .filter((v) => v >= 2)
    .length;
};

const addLine = (lineString: string, seafloor: OceanFloor) => {
  const line = parseLine(lineString);
  line.forEach(([x, y]) => {
    const prev = seafloor[`${x}_${y}`] || 0;
    seafloor[`${x}_${y}`] = prev + 1;
  });
  return seafloor;
};

const parseLine = (line: string): number[][] => {
  const [start, end] = line.split(" -> ");
  const [startx, starty] = start.split(",").map((e) => parseInt(e));
  const [endx, endy] = end.split(",").map((e) => parseInt(e));
  let result:number[][] = [];

  if (startx !== endx && starty !== endy) {
  } else if (startx === endx) {
    
    result = starty < endy ? parseVerticalLine(startx, starty, endy) : parseVerticalLine(startx, endy, starty);
  } else if (starty === endy) {
    result = startx < endx ? parseHorizontalLine(starty, startx, endx):parseHorizontalLine(starty, endx, startx) ;
  }
  return result;
};

const parseHorizontalLine = (y: number, start: number, end: number): number[][] => {
  const result = [];
  for (let i = start; i <= end; i++) {
    result.push([i, y]);
  }
  return result;
};

const parseVerticalLine = (x: number, start: number, end: number): number[][] => {
  const result = [];
  for (let i = start; i <= end; i++) {
    result.push([x, i]);
  }
  return result;
};

export { addLine, parseLine, solveDay5 };
