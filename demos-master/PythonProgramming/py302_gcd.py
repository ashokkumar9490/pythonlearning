def gcd(a, b):
    "greatest common divisor"
    while a != 0:
        a, b = b % a, a    # parallel assignment
    return b


print(gcd.__doc__)
print(gcd(12, 20))
print(gcd(20, 12))
print(gcd(5, 7))
