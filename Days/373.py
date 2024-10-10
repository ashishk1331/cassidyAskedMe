# Question 373

# Given a list of ingredients needed for a recipe,
# represented as strings, and a list of ingredients
# you have in your pantry, write a function to
# return the minimum number of additional ingredients
# you need to buy to make the recipe. If you want
# to do some extra credit, add expiration dates to
# the pantry items, and only account for food that
# isn't expired.
from datetime import date


def check_pantry(recipe, pantry):
    needed_ingredients_count = 0
    today = date.today()

    for ingredient in recipe:

        for item, expiry in pantry:
            expiry = date.fromisoformat(expiry)
            if item == ingredient and (expiry - today).days > 0:
                break
        else:
            needed_ingredients_count += 1

    return needed_ingredients_count


def main():
    # Test case 1: All ingredients are non-expired
    recipe = ["eggs", "flour", "sugar", "butter"]
    pantry = [
        ("eggs", "2025-01-01"),
        ("flour", "2024-12-31"),
        ("sugar", "2024-11-30"),
        ("butter", "2024-12-10"),
    ]
    assert check_pantry(recipe, pantry) == 0  # No ingredients needed

    # Test case 2: All ingredients are expired
    recipe = ["eggs", "flour", "sugar", "butter"]
    pantry = [
        ("eggs", "2022-01-01"),
        ("flour", "2023-06-01"),
        ("sugar", "2023-11-30"),
        ("butter", "2023-12-01"),
    ]
    assert check_pantry(recipe, pantry) == 4  # All ingredients needed

    # Test case 3: Some ingredients are expired
    recipe = ["eggs", "flour", "sugar", "butter"]
    pantry = [
        ("eggs", "2025-01-01"),
        ("flour", "2023-12-30"),
        ("sugar", "2024-11-30"),
        ("butter", "2023-12-01"),
    ]
    assert check_pantry(recipe, pantry) == 2  # Missing flour and butter (both expired)

    # Test case 4: Pantry has additional items, but some needed items are expired
    recipe = ["eggs", "flour", "sugar"]
    pantry = [
        ("eggs", "2025-01-01"),
        ("flour", "2022-12-31"),
        ("sugar", "2024-11-30"),
        ("milk", "2024-10-15"),
    ]
    assert (
        check_pantry(recipe, pantry) == 1
    )  # Missing flour (expired), other ingredients present

    # Test case 5: Some ingredients are missing and some are expired
    recipe = ["eggs", "flour", "sugar"]
    pantry = [("eggs", "2023-10-01"), ("milk", "2024-12-31"), ("butter", "2023-12-01")]
    assert check_pantry(recipe, pantry) == 3  # All ingredients missing or expired

    # Test case 6: Recipe with no ingredients (empty recipe)
    recipe = []
    pantry = [("eggs", "2025-01-01"), ("flour", "2024-12-31")]
    assert (
        check_pantry(recipe, pantry) == 0
    )  # No ingredients needed for an empty recipe

    # Test case 7: Pantry is empty, all ingredients needed
    recipe = ["eggs", "sugar", "butter"]
    pantry = []
    assert check_pantry(recipe, pantry) == 3  # All ingredients are needed

    # Test case 8: Pantry has expired ingredients only
    recipe = ["eggs", "flour", "sugar"]
    pantry = [("eggs", "2022-01-01"), ("flour", "2023-06-01"), ("sugar", "2023-11-30")]
    assert check_pantry(recipe, pantry) == 3  # All ingredients are expired, so needed


if __name__ == "__main__":
    main()
