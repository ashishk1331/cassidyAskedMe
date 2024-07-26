# Question 355

# Write a function that takes an array of integers 
# and returns a new array containing only the even 
# numbers, and sorted.

def onlyEvens(nums):
	return sorted(filter(lambda x: not x%2, nums))

def main():
	assert onlyEvens([1, 2, 3, 4, 5, 2]) == [2, 2, 4]
	assert onlyEvens([7, 8, 1, 0, 2, 5]) == [0, 2, 8]
	assert onlyEvens([11, 13, 15]) == []

if __name__ == '__main__':
	main()