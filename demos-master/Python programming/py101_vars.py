"""
x = 1
y = 'abc'
z = False
"""

principal = 1000  # Initial amount
rate = 0.05  # Interest rate
numyears = 5  # Number of years
year = 1
while year <= numyears:
    principal = principal * (1 + rate)
    # print(year, principal)  # Reminder: print(year, principal) in Python 3
    print("%3d %0.2f" % (year, principal))
    year += 1


x = globals()
print(x)            # global variable


def useLocal():
    y = 234         # local variable
    print(x)
    print(y)


print(x)
# print(y)          # error - "y" is not defined
