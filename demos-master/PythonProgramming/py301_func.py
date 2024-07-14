# def sum():
#     pass


# sum()


# getSum(22, 33)    can't call not defined yet


# def getSum(a, b):
#     print(a+b)


# getSum(22, 33)


# def getSum2(a, b):
#     return a+b


# print(getSum2(22, 33))        # positional arguments


# def getSum3(a, b):
#     print(f"a={a}, b={b}")
#     return a+b


# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that are sent to the function when it is called.

# print(getSum3(b=22, a=33))    # keyword/named arguments


# def getSum4(a=22, b=44):
#     print(f"a={a}, b={b}")      # a=33, b=44
#     return a+b                  # 77


# print(getSum4(a=33))
# print(getSum4(33))
# print(getSum4(b=55))
# print(getSum4(b=55, a=44))


# def ask_ok(prompt, retries=4, reminder='Please try again!'):
#     while True:
#         reply = input(prompt)
#         if reply in {'y', 'ye', 'yes'}:
#             return True
#         if reply in {'n', 'no', 'nop', 'nope'}:
#             return False
#         retries = retries - 1
#         if retries < 0:
#             print(f'invalid user response')
#             break
#         else:
#             print(reminder)


# ask_ok('Do you really want to quit?')

# def getSum5(*args):
#     sum = 0
#     for item in args:
#         sum += item
#     return sum


# print("getSum5 ", getSum5(11, 22, 33, 44))

# *args name is not mandatory, you can use any name

# def getSum6(*mult):
#     sum = 0
#     for item in mult:
#         sum += item
#     return sum


# print("getSum6 ", getSum6(11, 22, 33, 44))


# combining default and *args

# def concat(*args, sep="/"):
#     return sep.join(args)


# print(concat("Cat", "Dog", "Parrot", sep="$"))

# Positional argument cannot appear after keyword arguments
# print(concat(sep="$", "Cat", "Dog", "Parrot"))    # error


# a = 10


# def foo(x=a):
#     return x


# a = 5  # Reassign 'a'.
# print(foo())  # returns 10 (default value not changed)


# demo of **kwargs - it is used to pass a keyworded, variable-length argument list

# def getSum7(**kwargs):
#     if ('a' in kwargs):
#         print("a = ", kwargs['a'])
#     else:
#         print("'a' not provided")


# getSum7(a=11, b=22, c=33, d=44)
# getSum7(z=11, b=22, c=33, d=44)


# # getSum7 = lambda a, b: a+b
# # print(getSum7(5, 4))

# # use of lambda


def get_function(n):
    return lambda a: a * n

# get_function is returning another function


mytripler = get_function(3)

print(mytripler(11))


mydoubler = get_function(2)

print(mydoubler(11))

# def fib(n):  # write Fibonacci series up to n
#     """Print a Fibonacci series up to n."""
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a+b
#     print()


# fib(50)


# def fib2(n):  # write Fibonacci series up to n
#     """Print a Fibonacci series up to n."""
#     a, b = 0, 1
#     result = []
#     while a < n:
#         result.append(a)
#         a, b = b, a+b
#     return result


# result = fib2(50)
# print(result)
