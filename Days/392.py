# Question for Week 392
from typing import List


def findShieldBreak(attack: List[int], sheild: int) -> int:
    index, N = 0, len(attack)
    while index < N and sheild >= attack[index]:
        sheild -= attack[index]
        index += 1
    return -1 if index == N else index


def main():
    assert findShieldBreak([10, 20, 30, 40], 50) == 2
    assert findShieldBreak([1, 2, 3, 4], 20) == -1
    assert findShieldBreak([50], 30) == 0
    print("✅ All tests passed.")


if __name__ == "__main__":
    main()
