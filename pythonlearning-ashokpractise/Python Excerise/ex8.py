while True:
    try:
        list1 = [4,5,6]
        print(list1[2])
        x = int(input("enter a number:"))
        y = int(input("enter another number:"))
        div = x/y
    except ZeroDivisionError:
        print(" Zero divison error")
    except ValueError:
        print("Input value error")
        continue
    except:
        print("any other exception")
        break
    else:
      print(round(div,2))
      break
    finally:
      print("finally block")
      