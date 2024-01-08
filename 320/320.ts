/*
	Problem Statement:
	Given two integers source and target, add operators 
	in the source number to make it equal target, if possible. 
	You can return just one, or all possibilities for this!

	> addOperators(123, 6)
	> ["1*2*3", "1+2+3"]

	> addOperators(3456237490, 9191)
	> []
*/

/**
 * @param {number[]} number
 * @param {number} target
 * @returns {void}
 */
function addOperators(number: number, target: number): string[] {
	
	return [];
}

/**
 * IIFE main
 * @return {void}
 */
(function main(): void {
	// inputs are placed in this array
	let inputs: Array<Array<number>> = [
		[123, 6],
		[3456237490, 9191],
	];

	// for each input respective output is produced
	inputs.forEach((value: number[], index: number) => {
		console.log(`Running test for: [${value}]`);

		console.log(addOperators(value[0], value[1]));
	});
})();
