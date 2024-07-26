# Question 343

# Given an integer array arr, return the maximum 
# difference between two successive elements in 
# arr's sorted form. Return 0 if there's 0 or 1 
# elements.

def maxGap(nums):
	if len(nums) < 2:
		return 0

	nums.sort()
	gap = 0

	for index, number in enumerate(nums[:-1]):
		gap = max(gap, nums[index + 1] - number)

	return gap

def main():
	assert maxGap([3,6,9,1,2]) == 3

if __name__ == '__main__':
	main()