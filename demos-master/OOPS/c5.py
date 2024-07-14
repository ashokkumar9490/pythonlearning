class Class1:

    def __init__(self, val):
        print("Object Initialized")
        self.val = val

    def Display(self):
        print("Display Working")

    def __str__(self):
        return f"Object displayed using __str__ val = {self.val}"


o1 = Class1(10)
o2 = Class1(20)

print(o1)           # will use __str__ to display detailed output of object
print(o2)

# print(o1.val)
# print(o2.val)

# o1.Display()
# o2.Display()
