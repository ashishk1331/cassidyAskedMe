# Question

# Santa is conducting his daily roll call for the reindeer,
# but the printer has mistakenly printed all their names
# backwards. To take attendance properly, he urgently needs
# a tool to reverse the reindeer names and put them in
# alphabetical order! Can you help Santa?


def rollCall(array):
    return list(sorted(map(lambda x: x[::-1], array)))


def assertList(list1, list2):
    if len(list1) != len(list2):
        return False

    for index in range(len(list1)):
        if list1[index] != list2[index]:
            return False

    return True


def main():
    assert assertList(
        rollCall(["yzneT", "ydissaC", "enimA"]), ["Amine", "Cassidy", "Tenzy"]
    )

    assert assertList(
        rollCall(
            [
                "rennoD",
                "nexiV",
                "recnarP",
                "temoC",
                "neztilB",
                "recnaD",
                "dipuC",
                "rehsaD",
                "hploduR",
            ]
        ),
        [
            "Blitzen",
            "Comet",
            "Cupid",
            "Dancer",
            "Dasher",
            "Donner",
            "Prancer",
            "Rudolph",
            "Vixen",
        ],
    )

    assert assertList(rollCall(["A", "B", "C"]), ["A", "B", "C"])

    print("✅ All tests passed.")


if __name__ == "__main__":
    main()
