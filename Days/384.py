def countPerfectlyRoundCookies(num):
    fact = 1
    while num > 1:
        fact *= num
        num -= 1

    count = 0
    while True:
        q, r = divmod(fact, 10)
        if r > 0:
            break
        count += 1
        fact = q

    return count


def main():
    assert countPerfectlyRoundCookies(5) == 1
    assert countPerfectlyRoundCookies(10) == 2
    assert countPerfectlyRoundCookies(100) == 24


if __name__ == "__main__":
    main()
