# the order.py contains a constructor to create our order object, 
# takes in string and numerical values from the runner / controller
import runner

class order:
    def __init__(self, food, size, sauces, drink):
        self.foodObj = food
        self.sizeObj = size
        self.saucesObj = sauces
        self.drinkObj = drink

    def new_order(self):
        return f"Your order is {self.foodObj, self.sizeObj, self.saucesObj, self.drinkObj }"
input = new_order
new_order = orderConstructor []
