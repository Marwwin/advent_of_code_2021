const listToMostCommonBit = (listOfBinaries: string[]): string => {
  const lengthOfBinary = listOfBinaries[0].length;
  const mostCommonBits = [];
  for (let index = 0; index < lengthOfBinary; index++) {
    const mcb = mostCommonBitByIndex(listOfBinaries, index);
    mostCommonBits.push(mcb);
  }
  return mostCommonBits.join("");
};

const mostCommonBitByIndex = (
  listOfBinaries: string[],
  index: number
): string => {
  const column = listOfBinaries.flatMap((binary) => binary[index]);
  const numberOfSetBits = column.reduce(
    (total, n) => (total += parseInt(n)),
    0
  );
  return numberOfSetBits >= listOfBinaries.length / 2 ? "1" : "0";
};

const flipBits = (numberAsBits: string) => {
  return Array.from(numberAsBits)
    .map((n) => (n === "0" ? "1" : "0"))
    .join("");
};

const getPowerConsumption = (gamma: string, epsilon: string) => {
  const gammaInt = parseInt(gamma, 2);
  const epsilonInt = parseInt(epsilon, 2);
  return gammaInt * epsilonInt;
};

const numberWithMostCommonBits = (listOfBinaries:string[], mostCommon = true): string => {
    let result = listOfBinaries;
    for (let index = 0; index < listOfBinaries.length; index++) {
        let mcb = mostCommonBitByIndex(result,index);
        if (!mostCommon) mcb = mcb === "1" ? "0" : "1";
        result = result.filter(num => num[index] === mcb)
        if (result.length === 1) return result[0];
    }
    return ""
}

export {
  flipBits,
  getPowerConsumption,
  mostCommonBitByIndex,
  listToMostCommonBit,
  numberWithMostCommonBits
};
