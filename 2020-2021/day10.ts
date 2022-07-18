let inputs: number[] = [
	71,
	30,
	134,
	33,
	51,
	115,
	122,
	38,
	61,
	103,
	21,
	12,
	44,
	129,
	29,
	89,
	54,
	83,
	96,
	91,
	133,
	102,
	99,
	52,
	144,
	82,
	22,
	68,
	7,
	15,
	93,
	125,
	14,
	92,
	1,
	146,
	67,
	132,
	114,
	59,
	72,
	107,
	34,
	119,
	136,
	60,
	20,
	53,
	8,
	46,
	55,
	26,
	126,
	77,
	65,
	78,
	13,
	108,
	142,
	27,
	75,
	110,
	90,
	35,
	143,
	86,
	116,
	79,
	48,
	113,
	101,
	2,
	123,
	58,
	19,
	76,
	16,
	66,
	135,
	64,
	28,
	9,
	6,
	100,
	124,
	47,
	109,
	23,
	139,
	145,
	5,
	45,
	106,
	41
]

function countDiferences(diferences: number[]): number[] {

	let result: number[] = [0, 0, 0];

	for (let diference of diferences) {

		result[diference - 1] += 1;

	}

	result[2] += 1;

	return result;

}

function searchAdapter(inputs: number[], diferences: number[], actualVoltage: number): number[] {

	if (inputs.length) {

		let temporalValidAdapters: number[] = [];

		for (let adapter of inputs) {

			let diference = adapter - actualVoltage;

			if (diference >= 0 && diference <= 3) {

				temporalValidAdapters.push(adapter);

			}

		}

		let minVoltageAdapter = Math.min.apply(null, temporalValidAdapters);
		let finalDiference = minVoltageAdapter - actualVoltage;

		inputs.splice(inputs.indexOf(minVoltageAdapter), 1);

		if (finalDiference == 1 || finalDiference == 3) {

			diferences.push(finalDiference);

		}

		searchAdapter(inputs, diferences, minVoltageAdapter);

	}

	return diferences;

}

let combinations = 0;

function countCombinations(inputs: number[], actualVoltage: number) {

	let temporalValidAdapters: number[] = [];

	for (let adapter of inputs) {

		let diference = adapter - actualVoltage;

		if (diference >= 0 && diference <= 3) {

			temporalValidAdapters.push(adapter);

		}

	}

	if (temporalValidAdapters.length > 1) {

		if (combinations > 1) {

			combinations--;

		}

		combinations += temporalValidAdapters.length;

	}

	for (let option of temporalValidAdapters) {

		let copy = [...inputs];
		copy.splice(copy.indexOf(option), 1);

		countCombinations(copy, option);

	}

}

let results: Record<number, number> = { 0: 1 };

function countCombinations2(inputs: number[]) {

	for (let number of inputs) {

		results[number] = 0;

		if (results[number - 1]) {

			results[number] += results[number - 1]

		}


		if (results[number - 2]) {

			results[number] += results[number - 2]

		}


		if (results[number - 3]) {

			results[number] += results[number - 3]

		}

	}

}

function part1() {

	let result: number[] = searchAdapter(inputs, [], 0);
	let values: number[] = countDiferences(result);

	console.log(result, values, values[0] * values[2]);

}

function part2() {

	inputs = inputs.sort((a, b) => a - b);

	countCombinations2(inputs);

	console.log(results);

}

// part1();
part2();
