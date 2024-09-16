# Question 370

# You are given an integer n representing the total points
# a team wants to score in an American football game. You
# need to determine the number of unique ways the team can
# achieve exactly n points using any combination of
# touchdowns (6 points), field goals (3 points), or
# safeties (2 points).

visited = set()

def waysToScore(n, path = []):
    if n == 0:
        path = tuple(sorted(path))
        if path in visited:
            return 0
        visited.add(path)
        return 1

    if n < 0:
        return 0

    res = 0
    for point in [2, 3, 6]:
        path.append(point)
        res += waysToScore(n - point, path)
        path.pop()

    return res


def main():
    assert waysToScore(5) == 1
    assert waysToScore(12) == 6
    assert waysToScore(6) == 3


if __name__ == "__main__":
    main()
