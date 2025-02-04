from datetime import date


def newYearsDay(year):
    return date(year, 12, 31).strftime("%A")


def main():
    assert newYearsDay(2025) == "Wednesday"
    assert newYearsDay(2024) == "Tuesday"
    print("✅ All tests passed.")


if __name__ == "__main__":
    main()
