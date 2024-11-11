# Question 378


def seeBuildingsLeft(heights):
    if not heights:
        return 0

    max_num, count = heights[0], 1

    for height in heights:
        if height > max_num:
            max_num = height
            count += 1

    return count


def main():
    # Original test cases
    assert seeBuildingsLeft([1, 2, 3, 4, 5]) == 5
    assert seeBuildingsLeft([5, 4, 3, 2, 1]) == 1
    assert seeBuildingsLeft([3, 7, 8, 3, 6, 1]) == 3

    # New test cases
    # Single building: only 1 building is visible
    assert seeBuildingsLeft([10]) == 1

    # All buildings of equal height: only the first building is visible
    assert seeBuildingsLeft([3, 3, 3, 3, 3]) == 1

    # Alternating heights: 1st, 3rd, and 5th buildings are visible
    assert seeBuildingsLeft([1, 3, 2, 4, 3, 5]) == 4

    # Strictly increasing heights with gaps
    assert seeBuildingsLeft([2, 5, 10, 20, 50]) == 5

    # Mixed heights, only some buildings are visible from the left
    assert seeBuildingsLeft([4, 2, 7, 1, 9, 3, 10]) == 4

    # Edge case: empty list of buildings
    assert seeBuildingsLeft([]) == 0

    # Edge case: building heights in descending order with a peak at the end
    assert seeBuildingsLeft([10, 8, 6, 4, 2, 12]) == 2

    # Heights with a tall building at the beginning followed by shorter ones
    assert seeBuildingsLeft([9, 1, 2, 3, 4]) == 1

    # Sequence where only the first and the last buildings are visible
    assert seeBuildingsLeft([7, 3, 5, 6, 10]) == 2

    print("All test cases passed!")


if __name__ == "__main__":
    main()
