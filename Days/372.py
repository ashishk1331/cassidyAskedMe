# Question 372

# Implement your own String split() function
# in your preferred programming language.

from typing import List


def split(string: str, delimiter: str) -> List[str]:
    string += delimiter

    chunks, buffer = [], ""
    index, n, m = 0, len(string), len(delimiter)
    strange_behaviour = False

    if n - m == 0:
        return [""]
    if m == 0:
        strange_behaviour = True

    while index < n:
        char = string[index]

        if strange_behaviour:
            chunks.append(char)
        elif char == delimiter[0] and string[index : index + m] == delimiter:
            index += m - 1
            chunks.append(buffer)
            buffer = ""
        else:
            buffer += char

        index += 1

    return chunks


def main():
    # Test case 1: Standard case with space as delimiter
    sample: str = "This is so, so silly!"
    assert split(sample, " ") == ["This", "is", "so,", "so", "silly!"]

    # Test case 2: Empty delimiter, should split into individual characters
    assert split(sample, "") == [
        "T",
        "h",
        "i",
        "s",
        " ",
        "i",
        "s",
        " ",
        "s",
        "o",
        ",",
        " ",
        "s",
        "o",
        " ",
        "s",
        "i",
        "l",
        "l",
        "y",
        "!",
    ]

    # Test case 3: Comma delimiter, splitting on commas
    assert split(sample, ",") == ["This is so", " so silly!"]

    # Test case 4: Splitting with a substring that does not exist in the string
    assert split(sample, "x") == ["This is so, so silly!"]

    # Test case 5: Empty string input
    assert split("", " ") == [""]

    # Test case 6: Delimiter at the beginning and end of the string
    assert split(" hello ", " ") == ["", "hello", ""]

    # Test case 7: Multiple consecutive delimiters
    assert split("word1,,word2", ",") == ["word1", "", "word2"]

    # Test case 8: Delimiter is a character that appears multiple times
    assert split("apple|banana|cherry", "|") == ["apple", "banana", "cherry"]

    # Test case 9: Delimiter longer than one character
    assert split("a-b--c", "--") == ["a-b", "c"]

    # Test case 10: No delimiters in the string
    assert split("HelloWorld", ",") == ["HelloWorld"]

    # Test case 11: One-character string with delimiter
    assert split("x", "x") == ["", ""]

    # Test case 12: Splitting a string with a multi-character delimiter that isn't found
    assert split("NoDelimiterHere", "//") == ["NoDelimiterHere"]

    # Test case 13: Splitting on a number as a delimiter
    assert split("1234-5678", "-") == ["1234", "5678"]

    # Test case 14: Empty delimiter but with an empty string
    assert split("", "") == [""]

    # Test case 15: Delimiter is a space but input string has no spaces
    assert split("NoSpacesHere", " ") == ["NoSpacesHere"]

    print("All test cases passed!")


if __name__ == "__main__":
    main()
