# Question 353

# The Spanish language uses inverted punctuation marks (¿ and ¡)
# in interrogative and exclamatory sentences. Write a function
# that takes in a string str, and adds ¿ and ¡ if they're needed.
# You can ignore exclamations in the middle of a sentence for
# this problem.

dmap = {"!": "¡", "?": "¿"}


def fixInvertedPunc(string):
    result = []
    temp = []

    for word in string.split():
        temp.append(word)

        if word.endswith("!") or word.endswith("?"):

            if not temp[0].startswith(dmap[word[-1]]):
                temp[0] = dmap[word[-1]] + temp[0]

            result.extend(temp)
            temp = []

    return " ".join(result)


def main():
    assert fixInvertedPunc("Feliz cumpleaños!") == "¡Feliz cumpleaños!"
    assert (
        fixInvertedPunc("Ella ya se graduó de la universidad? ¡No!")
        == "¿Ella ya se graduó de la universidad? ¡No!"
    )


if __name__ == "__main__":
    main()
