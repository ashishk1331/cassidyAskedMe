from typing import List
from itertools import permutations


def findAnagrams(s: str, t: str) -> List[int]:
    anagrams = list(map("".join, permutations(t)))

    results = []
    for index in range(len(s) - len(t) + 1):
        if any([s[index:].startswith(word) for word in anagrams]):
            results.append(index)

    return results


def main():
    assert findAnagrams("cbaebabacd", "abc") == [0, 6]
    assert findAnagrams("fish", "cake") == []
    assert findAnagrams("abab", "ab") == [0, 1, 2]
    print("✅ All Tests Passed.")


if __name__ == "__main__":
    main()
