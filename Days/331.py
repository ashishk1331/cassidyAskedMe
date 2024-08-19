# Question 331

# Write a function that determines if an array of
# numbers is a bitonic sequence. A bitonic sequence
# is a sequence of numbers in which the numbers are
# in increasing order, and after a certain point,
# they start decreasing. Extra credit: print the
# peak number in the sequence!


def isBitonic(nums):
    pass


def main():
    assert isBitonic([1, 2, 3, 2]) == (True, 3)
    assert isBitonic([1, 2, 3]) == (False, -1)
    assert isBitonic([3, 4, 5, 5, 5, 2, 1]) == (True, 5)


if __name__ == "__main__":
    main()
