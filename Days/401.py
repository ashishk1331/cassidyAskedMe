def calculateIngredients(ingregs, times):
    return list(
        map(lambda ing: {"name": ing["name"], "amount": ing["amount"] * times}, ingregs)
    )


def main():
    ingredients = [
        {"name": "flour", "amount": 200},
        {"name": "sugar", "amount": 100},
        {"name": "eggs", "amount": 2},
    ]
    targetServings = 3
    print(calculateIngredients(ingredients, targetServings))


if __name__ == "__main__":
    main()
