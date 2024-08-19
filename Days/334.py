from itertools import permutations


def solve(array):
    seen = set()
    total = 0
    for i in range(1, len(array) + 1):
        for each in permutations(array, i):
            seq = "".join(each)
            if seq in seen:
                continue
            total += 1
            seen.add(seq)

    return total


print(solve(["X"]))  # 1
print(solve(["A", "A", "B"]))  # 8
