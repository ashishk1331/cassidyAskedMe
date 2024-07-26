# Question 360

# Write a function that takes an array of integers 
# representing the number of flowers planted in a line, 
# and an integer k representing the number of additional 
# flowers you want to plant. Return whether it's possible 
# to plant all k flowers without planting any two flowers 
# adjacent to each other.

def canPlantFlowers(row, count) -> bool:
	if not row[0] and not row[1]:
		row[0] = 1
		count -= 1

	for index, _ in enumerate(row[1:-1], 1):
		if count == 0:
			return True

		if (row[index - 1] + row[index + 1] + row[index]) == 0:
			row[index] = 1
			count -= 1

	if not row[-2] and not row[-1]:
		row[-1] = 1
		count -= 1

	return count == 0



def main():
	assert canPlantFlowers([1, 0, 0, 0, 1], 1) == True
	assert canPlantFlowers([1, 0, 0, 0, 1], 2) == False
	assert canPlantFlowers([0, 0, 0, 0, 0], 3) == True
	assert canPlantFlowers([1, 0, 1, 0, 1], 1) == False

if __name__ == '__main__':
	main()