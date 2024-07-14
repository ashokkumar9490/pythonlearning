class Class1:

    def __init__(self, val):
        print("Object Initialized")
        self.val = val

    def Display(self):
        print("Display Working")

    def __str__(self):
        return "Object displayed using __str__"

    def __repr__(self):         # to copy the object
        return f"Class1('{self.val}')"  # "Class1(10)"


o1 = Class1(10)
o2 = Class1(20)
o3 = eval(repr(o2))

print(o1)
print(o2)
print(o3)

print(o1.val)
print(o2.val)
print(o3.val)

print(id(o1))
print(id(o2))
print(id(o3))


# o1.Display()
# o2.Display()
