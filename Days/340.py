# Question 340

# Given a string array, find the maximum product
# of word lengths where the words don't share any
# letters.

from itertools import combinations


def wordLengthProduct(words):
    dmap = {word: set(word) for word in words}
    prod = 0

    for first, last in combinations(words, 2):
        if not (dmap[first] & dmap[last]):
            prod = max(prod, len(first) * len(last))

    return prod


def main():
    assert (
        wordLengthProduct(["fish", "fear", "boo", "egg", "cake", "abcdef"]) == 16
    )  # "fish" and "cake"
    assert wordLengthProduct(["a", "aa", "aaa", "aaaa"]) == 0


if __name__ == "__main__":
    main()
