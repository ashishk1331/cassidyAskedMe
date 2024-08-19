def getDMAP():
    dmap = {}
    rows = [
        ["wertyuiop[", "qwertyuiop"],
        ["sdfghjkl;", "asdfghjkl"],
        ["xcvbnm,", "zxcvbnm"],
    ]

    for row in rows:
        n = len(row[0])
        for index in range(n):
            dmap[row[0][index]] = row[1][index]

    return dmap


def translateRightShift(string):
    dmap = getDMAP()
    res = ""
    for char in string:
        if char in dmap:
            res += dmap[char]
        else:
            res += char
    return res


def main():
    assert translateRightShift(";p; epeor") == "lol wowie"
    assert translateRightShift("ejp s, o") == "who am i"


if __name__ == "__main__":
    main()
