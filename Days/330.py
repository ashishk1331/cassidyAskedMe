# [Todo] Boyer-Moore Voting Algorithm

import collections


def majority(array):
    dmap = collections.defaultdict(lambda: 0)

    for each in array:
        dmap[each] += 1

    que = sorted(dmap.items(), key=lambda x: x[1], reverse=True)

    half = len(array) // 2

    if que[0][1] >= half:
        return que[0][0]

    odd, even = 0, 0
    for num, times in que:
        if num % 2:
            odd += 1
        else:
            even += 1

    if odd == even:
        return "No majority"
    elif odd > even:
        return "Majority Odd"
    return "Majority Even"


def main():
    arrays = [
        [3, 1, 4, 1],
        [33, 44, 55, 66, 77],
        [1, 2, 3, 4],
    ]

    for each in arrays:
        print(majority(each))


if __name__ == "__main__":
    main()
