# Question 356

# Write a function that takes an array of integers
# and a target sum, and returns all unique quadruplets
# [a, b, c, d] in the array such that a + b + c + d = target.
# If it's impossible, return an empty array.


def fourSum(nums, count):
    pass


def main():
    assert fourSum([1, 0, -1, 0, -2, 2], 0) == [
        [-2, -1, 1, 2],
        [-2, 0, 0, 2],
        [-1, 0, 0, 1],
    ]
    assert fourSum([], 0) == []
    assert fourSum([1, -2, -5, -4, -3, 3, 3, 5], -11) == [[-5, -4, -3, 1]]


if __name__ == "__main__":
    main()
