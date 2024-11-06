# Question 377

# Given an array of strings, group the anagrams together.

from collections import defaultdict
from itertools import chain


def groupAnagrams(words):
    legend = defaultdict(list)

    for word in words:
        footprint = tuple(sorted(word))
        legend[footprint].append(word)

    return list(legend.values())


def s(nested_list):
    return "".join(chain.from_iterable(nested_list))


def main():
    # Basic test case with multiple anagrams and unique words
    assert s(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) == s(
        [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    )

    # Test case with no anagrams
    assert s(groupAnagrams(["vote", "please"])) == s([["vote"], ["please"]])

    # Test case with one pair of anagrams
    assert s(groupAnagrams(["debitcard", "badcredit"])) == s(
        [["debitcard", "badcredit"]]
    )

    # Test case with an empty list
    assert groupAnagrams([]) == []

    # Test case with single character words (each word is its own group)
    assert s(groupAnagrams(["a", "b", "c", "a"])) == s([["a", "a"], ["b"], ["c"]])

    # Test case with repeated anagrams
    assert s(groupAnagrams(["listen", "silent", "enlist", "google", "glegoo"])) == s(
        [["listen", "silent", "enlist"], ["google", "glegoo"]]
    )

    # Test case with mixed-case words (treats differently based on case)
    assert s(groupAnagrams(["Eat", "Tea", "ate", "Nat", "Tan", "bat"])) == s(
        [["Eat"], ["Tea"], ["ate"], ["Nat", "Tan"], ["bat"]]
    )

    # Test case with very long words
    assert s(groupAnagrams(["a" * 1000, "a" * 1000, "b" * 1000])) == s(
        [["a" * 1000, "a" * 1000], ["b" * 1000]]
    )

    # Test case with numeric strings as input
    assert s(groupAnagrams(["123", "231", "312", "456", "564"])) == s(
        [["123", "231", "312"], ["456", "564"]]
    )

    print("All tests passed!")


if __name__ == "__main__":
    main()
