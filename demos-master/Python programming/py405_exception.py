"""Module to demonstrate exception handling in Python"""


try:
    x = int(input("Enter a number: "))
except ValueError as ve:
    print("Input Value Error ")
else:
    print("You entered ", x)
