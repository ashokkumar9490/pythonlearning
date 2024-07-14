# def outer(x):
#     def inner(y):
#         return x + y
#     return inner


# add_five = outer(5)
# result = add_five(6)
# print(result)  # prints 11


# add_ten = outer(10)
# result = add_ten(6)
# print(result)  # prints 16


# def add(x, y):
#     return x + y


# def sub(x, y):
#     return x - y


# def calculate(func, x, y):
#     return func(x, y)


# result = calculate(add, 4, 6)
# print(result)  # prints 10

# result = calculate(sub, 4, 6)
# print(result)  # prints -2

# num1 = 11
# print(num1.__add__(22))

# demo of map function


# string = "ABCDEF"
# ch_iterator = iter(string)

# print(next(ch_iterator))  #A
# print(next(ch_iterator))  # B
# print(next(ch_iterator))


# def square(x):
#     return x * x

# numbers = [1, 2, 3, 4, 5]       # list
# squared = list(map(square, numbers))   # convert collection to list
# print(squared)


numbers = [1, 2, 3, 4, 5]       # list
squared = list(map(lambda x: x*x, numbers))   # convert collection to list
print(squared)
