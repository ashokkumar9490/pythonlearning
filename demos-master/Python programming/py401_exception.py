"""Module to demonstrate exception handling in Python"""

while True:
    try:
        # open('xyz.txt')
        # list1 = [4, 5, 6]
        # print(list1[5])
        x = int(input("Enter a number: "))
        y = int(input("Enter another number: "))
        div = x/y

    except ZeroDivisionError:
        print("Zero Division Error")
    except IOError:
        print("Can't open File")
        break
    except ValueError:
        print("Input Value Error")
        continue
    except (TypeError, NameError):
        pass
    except:         # catch all exceptions block
        print("Any other exception")
        break
    else:
        print(round(div, 2))
        break
    finally:
        print("Finally block")

# demonstrate exception handling in Python, also demo use of pylint
