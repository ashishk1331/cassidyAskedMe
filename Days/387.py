def natoify(
    s: str,
    is_british: bool = False,
    is_indonesian: bool = False,
    is_filipino: bool = False,
    is_american: bool = False,
    is_atc: bool = False,
    is_old: bool = False,
) -> str:
    phonetic_dict = {
        "A": "Alfa",
        "B": "Bravo",
        "C": "Charlie",
        "D": "Delta",
        "E": "Echo",
        "F": "Foxtrot",
        "G": "Golf",
        "H": "Hotel",
        "I": "India",
        "J": "Juliett",
        "K": "Kilo",
        "L": "Lima",
        "M": "Mike",
        "N": "November",
        "O": "Oscar",
        "P": "Papa",
        "Q": "Quebec",
        "R": "Romeo",
        "S": "Sierra",
        "T": "Tango",
        "U": "Uniform",
        "V": "Victor",
        "W": "Whiskey",
        "X": "Xray",
        "Y": "Yankee",
        "Z": "Zulu",
        "1": "One",
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Five",
        "6": "Six",
        "7": "Seven",
        "8": "Eight",
        "9": "Nine",
        "0": "Zero",
        " ": "(space)",
    }

    if is_old:
        phonetic_dict["N"] = "Nectar"

    if is_british:
        phonetic_dict["I"] = "Indigo"

    if is_indonesian:
        phonetic_dict["L"] = "London"

    if is_filipino:
        phonetic_dict["H"] = "Hawk"

    if is_american:
        phonetic_dict["F"] = "Fox"

    if is_atc:
        phonetic_dict["D"] = "David"

    return " ".join([phonetic_dict[char.upper()] for char in s])


def main():
    assert (
        natoify("hello world")
        == "Hotel Echo Lima Lima Oscar (space) Whiskey Oscar Romeo Lima Delta"
    )
    assert (
        natoify("3spooky5me")
        == "Three Sierra Papa Oscar Oscar Kilo Yankee Five Mike Echo"
    )

    print("✅ All tests passed.")


if __name__ == "__main__":
    main()
