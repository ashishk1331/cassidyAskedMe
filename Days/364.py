# Question 364

# Create a function that should take one argument n, which 
# is a positive integer. The function should return the sum 
# of all squared positive integers between 1 and n, inclusive.

def squares(n: int) -> int:
	return int((n*(n+1)*(2*n+1)) / 6)

def main():
	assert squares(5) == 55
	assert squares(10) == 385
	assert squares(25) == 5525
	assert squares(100) == 338350

if __name__ == '__main__':
	main()