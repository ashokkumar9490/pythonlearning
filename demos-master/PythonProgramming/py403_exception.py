"""Module to demonstrate exception handling in Python"""

try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    div = x/y

except ZeroDivisionError:
    print("Zero Division Error")
except ValueError:
    print("Input Value Error")
except:
    print("Any other exception")
else:
    print(div)
