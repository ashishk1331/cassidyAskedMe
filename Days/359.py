# Question 359

# Define a FruitStand class that allows you
# to add different types of fruits with their
# quantities and prices, update them, and
# calculate the total value of all the fruits
# in the stand.

# Implement the following methods:
# addFruit(name, quantity, price),
# updateQuantity(name, quantity), and
# totalValue()!


class Fruit:
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price

    def updateQuantity(self, newQuantity):
        self.quantity = newQuantity


class FruitStand:
    def __init__(self):
        self.stand = {}

    def addFruit(self, name, quantity, price):
        self.stand[name] = Fruit(quantity, price)

    def updateQuantity(self, name, quantity):
        self.stand[name].updateQuantity(quantity)

    def totalValue(self):
        total = 0

        for fruit in self.stand.values():
            total += fruit.quantity * fruit.price

        return total


def main():
    # // Create a new fruit stand
    stand = FruitStand()

    # // Add fruits to the stand
    stand.addFruit("apple", 10, 0.5)
    stand.addFruit("banana", 5, 0.2)
    stand.addFruit("cherry", 20, 0.1)

    # // Update the quantity of an existing fruit
    stand.updateQuantity("banana", 10)

    # // Calculate the total value of all fruits in the stand
    assert stand.totalValue() == 9.0


if __name__ == "__main__":
    main()
