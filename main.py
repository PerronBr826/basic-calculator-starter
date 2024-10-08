import random

# Bryce Perron, Charles Petoskey
# Basic Calculator


print("""Hello, welcome to my Basic Calculator!
      This script will prompt you to enter two numbers
      and then add, subtract, multiply or divide the numbers
      depending on what menu option you select.
      You can also do a random operation.
      """)

print("""Choose a math operator to preform:
      1. Addition (+)
      2. Subtraction (-)
      3. Multiplication (*)
      4. Division (/)
      5. Random (?)""")

operator = int(input("Enter your choice (1-5): "))

if operator == 5:
    operator = random.randint(1,4)
    number1 = random.randint(1,100)
    number2 = random.randint(1,100)
else:
    number1 = float(input("Please enter your first number: "))
    number2 = float(input("Please enter your second number: "))

if operator == 1:
    print(f"{number1} added to {number2} is {number1+number2}.")
elif operator == 2:
    print(f"{number1} subtracted from {number2} is {number1-number2}.")
elif operator == 3:
    print(f"{number1} multiplied by {number2} is {number1*number2}.")
elif operator == 4:
    print(f"{number1} divided by {number2} is {number1/number2}.")
else:
    print(f'"{operator}" is not a valid operator.')
