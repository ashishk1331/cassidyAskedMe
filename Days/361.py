def increasingSubsequence(nums):
	if len(nums) < 2:
		return len(nums)

	maxLen = 1
	count = 1
	temp = nums[0]

	for i in nums[1:]:
		if temp < i:
			count += 1
		else:
			maxLen = max(count, maxLen)
			count = 1
		temp = i
	
	if count > maxLen:
		return count
	return maxLen



def main():
	assert increasingSubsequence([10, 9, 2, 3, 7, 101, 18]) == 4
	assert increasingSubsequence([4, 4, 4, 3]) == 1

	# chatGPT generated test cases
	assert increasingSubsequence([10, 9, 2, 3, 7, 101, 18]) == 4
	assert increasingSubsequence([0, 1, 0, 3, 2, 3]) == 2
	assert increasingSubsequence([7, 7, 7, 7, 7, 7, 7]) == 1
	assert increasingSubsequence([2, 15, 3, 7, 8, 6, 18]) == 3
	assert increasingSubsequence([1, 2, 3, 4, 5]) == 5
	assert increasingSubsequence([5, 4, 3, 2, 1]) == 1
	assert increasingSubsequence([1, 3, 6, 7, 9, 4, 10, 5, 6]) == 5
	assert increasingSubsequence([10, 22, 9, 33, 21, 50, 41, 60, 80]) == 3
	assert increasingSubsequence([]) == 0
	assert increasingSubsequence([1]) == 1

if __name__ == '__main__':
	main()