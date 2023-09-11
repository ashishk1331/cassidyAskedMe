/*
	Problem Statement:
	Given an array of integers, sort them 
	into two separate sorted arrays of even 
	and odd numbers. If you see a zero, skip it.

	> separateAndSort([4,3,2,1,5,7,8,9])
	> [[2,4,6], [1,3,5,7,9]]

	> separateAndSort([1,1,1,1])
	> [[], [1,1,1,1]]
*/

/**
 * @param {number[]} nums
 * @param {number} num
 * @returns {void}
*/
function insertAtPos(nums: number[], num: number): void {
	if(nums.length < 1){
		nums.push(num);
	} else {
		let index = nums.length - 1;
		while(index > -1){
			if(num > nums[index]){
				break;
			}
			index -= 1;
		}
		nums.splice(index+1, 0, num);
	}
}

/**
 * @param {array} nums
 * @return {[array, array]}
 */
function separateAndSort(nums: number[]): [number[], number[]] {
	let even: number[] = [], odd: number[] = [];
	for (let num of nums) {
		if (num === 0) {
			continue;
		} else if (num % 2 === 0) {
			insertAtPos(even, num);
		} else {
			insertAtPos(odd, num);
		}
	}
	return [even, odd];
}

/**
 * IIFE main
 * @return {void}
 */
(function main(): void {
	// inputs are placed in this array
	let inputs: Array<Array<number>> = [
		[4, 3, 2, 1, 5, 7, 8, 9],
		[1, 1, 1, 1],
	];
	let results: Array<[Array<number>, Array<number>]> = [
		[
			[2, 4, 6],
			[1, 3, 5, 7, 9],
		],
		[[], [1, 1, 1, 1]],
	];

	// for each input respective output is produced
	inputs.forEach((value: Array<number>, index: number) => {
		let nums: Array<number> = value;
		let ans: [Array<number>, Array<number>] = separateAndSort(nums);
		console.log(ans);
		// let result: Array<[Array<number>, Array<number>]> = results[index];
		// let test: boolean =
		// 	ans.length === result.length &&
		// 	ans.every((value, index) => value === result[index]);
		// console.log(
		// 	test
		// 		? `✅ Test no. ${index + 1}: Passed`
		// 		: `❌ Test no. ${index + 1}: Failed`,
		// );
	});
})();
