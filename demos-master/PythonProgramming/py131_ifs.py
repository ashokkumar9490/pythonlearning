# x = 8
# if x == 5:
#     print('x=5')
# elif x > 5:
#     print('x>5')
# else:
#     print('x<5')


x = input("Enter a number: ")       # -a345
if x.lstrip('+-').isdigit():
    print("You entered a number")
    x = int(x)      # to avoid exception
    if (x < 0):
        print("You entered a negative number")
        x = 0
    elif (x > 0):
        print("You entered a positive number")
    elif (x == 0):
        print("You entered zero")
else:
    print("You entered a string")
