def permute(string):
    n = len(string)
    visited = set()
    result = []

    def backtrack(perm):
        if len(perm) == n:
            return result.append(perm)

        res = ""
        for index in range(n):
            if index not in visited:
                visited.add(index)
                backtrack(perm + string[index])
                visited.remove(index)

    backtrack("")
    return result


def main():
    assert permute("abc") == ["abc", "acb", "bac", "bca", "cab", "cba"]
    print("✅ All tests passed.")


if __name__ == "__main__":
    main()
