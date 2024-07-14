"""Module to demonstrate exception handling in Python"""
import traceback


def my_func():
    print("Function called...")
    while True:
        try:
            raise IOError("Raised an explicit exception")
        except ValueError:
            print("Input Value Error")


try:
    print("Starting point of execution")
    my_func()
except:         # handle all exceptions
    print("Exception Handled in main call", traceback.print_exc())
