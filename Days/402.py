def compress(chars):
    chars.append(None)
    res = []
    count = 1
    for i in range(1, len(chars)):
        if chars[i] == chars[i - 1]:
            count += 1
        else:
            res.append(chars[i - 1])
            if count > 1:
                res.append(str(count))
            count = 1
    return res


def main():
    assert compress(["a", "b", "b", "b", "c"]) == ["a", "b", "3", "c"]
    assert compress(["a", "a", "b", "b", "c", "c", "c"]) == [
        "a",
        "2",
        "b",
        "2",
        "c",
        "3",
    ]
    print("✅ All tests passed.")


if __name__ == "__main__":
    main()
