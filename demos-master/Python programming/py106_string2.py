str = "***abcd---"
print(str.lstrip('*'))  # abcd---
print(str.rstrip('-'))  # ***abcd
print(str.strip('-*'))  # abcd
print(str.ljust(20, '$'))   # actual str on left padding on the right
print(str.rjust(20, '$'))
print(str.center(21, '$'))  # for odd left side 1 extra
print(str.replace('a', 'z'))
print(str.upper())          # ABCD
print(str.lower())          # abcd
print(str.title())
print(str.capitalize())
print(str.swapcase())

str1 = "python language"
print(str1.title())         # every word first char upper
print(str1.capitalize())    # only first char upper
