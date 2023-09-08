/*
	Problem Statement:
	Given an array of integers and a number k 
	(where k is guaranteed to be less than the 
	array's length), return a subarray of length 
	k with the minimum possible sum. Maintain the 
	order of the original array!

	> minSubs([1,3,20,4,8,9,11], 3)
	> [4,8,9]

	> minSubs([4,4,4,4,8], 2)
	> [4,4]
*/

/**
 * @param {array} nums
 * @param {number} k
 * @return {array}
 */
function minSubs(nums: Array<number>, k: number): Array<number> {
	let start: number = 0,
		end: number = k,
		sum: number = 0;
	for (let i = 0; i < k; i++) {
		sum += nums[i];
	}
	for (let i = k; i < nums.length; i++) {
		let first: number = i - k;
		let newSum: number = sum - nums[first] + nums[i];
		if (newSum < sum) {
			start = first + 1;
			end = i + 1;
		}
		sum = newSum;
	}
	return nums.slice(start, end);
}

/**
 * IIFE main
 * @return {void}
 */
(function main(): void {
	// inputs are placed in this array
	let inputs: Array<[Array<number>, number]> = [
		[[1, 3, 20, 4, 8, 9, 11], 3],
		[[4, 4, 4, 4, 8], 2],
	];
	let results: Array<Array<number>> = [
		[4, 8, 9],
		[4, 4],
	];

	// for each input respective output is produced
	inputs.forEach((value: [Array<number>, number], index: number) => {
		let [nums, k]: [Array<number>, number] = value;
		let ans: Array<number> = minSubs(nums, k);
		let result: Array<number> = results[index];
		let test: boolean =
			ans.length === result.length &&
			ans.every((value, index) => value === result[index]);
		console.log(
			test
				? `✅ Test no. ${index + 1}: Passed`
				: `❌ Test no. ${index + 1}: Failed`,
		);
	});
})();
