def returnGift(date_string):
    months = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ]
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month, day, year = date_string.replace(",", "").split(" ")
    month, day, year = months.index(month) + 1, int(day), int(year)

    if month == 12:
        day += 90
    else:
        day += 30

    def isLeap(year):
        return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

    while day > days[month - 1] or month > 12:
        if day > days[month - 1]:

            if month == 2 and isLeap(year):
                day -= 29
            else:
                day -= days[month - 1]

            month += 1

        if month > 12:
            month = 1
            year += 1

    return f"{months[month - 1]} {day}, {year}"


def main():
    date_string = "Dec 25, 2023"
    print(returnGift(date_string))


if __name__ == "__main__":
    main()
