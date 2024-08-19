# Question 358

# Write a function that takes an array of daily temperatures
# and returns an array where each element is the number of days
# you would have to wait until a warmer temperature. If there
# is no future day for which this is possible, put 0 instead.


def dailyTemperatures(temp):
    pass


def main():
    assert dailyTemperatures([70, 70, 70, 75]) == [3, 2, 1, 0]
    assert dailyTemperatures([90, 80, 70, 60]) == [0, 0, 0, 0]
    assert dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [
        1,
        1,
        4,
        2,
        1,
        1,
        0,
        0,
    ]


if __name__ == "__main__":
    main()
