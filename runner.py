# The runner contains the code to Create a User Interface for the Cafe to interact with
# This 'runs' the code and will interact with the Controller directly
from controller import insertOrder

num1 = """(-------- Welcome to QA Cafe --------
What can we help you with?
1) Place an Order
2) Read Order By ID
3) Read All Orders
4) Update Order by ID
5) Delete Order by ID
6) Delete All Orders")"""
print (num1)
num1 = int(input("Please enter choice"))

if num1 == 1:
    
    name = input("what is your name?")
    main = input("What would you like to eat?")
    size = input("What size would you like?")
    sauce = input("what sauce would u like with that?")
    drink = input ("what drink would you like with that?")
    
    order = [name, main, size, sauce, drink]
    insertOrder(order)

elif num1 == 2:
    print("it works.... ish")
   
