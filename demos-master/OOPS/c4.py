class Class1:

    def __init__(self, val2):            # instance constructor
        print("Object Initialized")
        self.val = val2                 # val is instance attribute

    def Display(self):                  # instance function
        print(f"Display Working val = {self.val}")


o1 = Class1(10)
o2 = Class1(20)

x = 10
print(x)

print(o1)
print(o2)

# o1.Display()
# o2.Display()
