# Question 346

# Given an array of numbers, add all of
# the values together but only if the
# number doesn't repeat a digit.


def isUnique(num):
    numString = str(num)
    visited = set()

    for i in numString:
        if i in visited:
            return False
        else:
            visited.add(i)

    return True


def uniqueSum(nums):
    total = 0

    for each in nums:
        if isUnique(each):
            total += each

    return total


def main():
    assert uniqueSum([1, 2, 3]) == 6
    assert uniqueSum([11, 22, 33]) == 0
    assert uniqueSum([101, 2, 3]) == 5


if __name__ == "__main__":
    main()
