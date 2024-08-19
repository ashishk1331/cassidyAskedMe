# Question 344

# Given an integer array, write a function hills(arr)
# and a function valleys(arr) that return the number
# of hills and valleys, respectively, in the array.
# The integers represent heights!


def hills(heights):
    pass


def valleys(heights):
    pass


def main():

    # [1,2,1]
    assert hills([1, 2, 1]) == 1
    assert valleys([1, 2, 1]) == 0

    # [1,0,1]
    assert hills([1, 0, 1]) == 0
    assert valleys([1, 0, 1]) == 1

    # [7,6,5,5,4,1]
    assert hills([7, 6, 5, 5, 4, 1]) == 0
    assert valleys([7, 6, 5, 5, 4, 1]) == 0

    # [3,4,1,1,6,5]
    assert hills([3, 4, 1, 1, 6, 5]) == 2
    assert valleys([3, 4, 1, 1, 6, 5]) == 1


if __name__ == "__main__":
    main()
