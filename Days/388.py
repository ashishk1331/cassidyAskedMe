def longestSubsequence(nums):
    n = len(nums)

    if n < 2:
        return n

    i = j = 0
    temp = count = 1
    while j < n - 1:
        if abs(nums[j] - nums[j + 1]) == 1:
            temp += 1
        else:
            count = max(count, temp)
            temp = 1
            i = j
        j += 1

    if j > i:
        count = max(count, temp)
    return count


def main():
    assert longestSubsequence([1, 2, 3, 4, 5]) == 5
    assert longestSubsequence([4, 2, 3, 1, 5]) == 2
    assert longestSubsequence([10, 11, 7, 8, 9, 12]) == 3
    print("✅ All tests passed.")


if __name__ == "__main__":
    main()
