class Class1:

    def __init__(self, val):
        print("Object Initialized")
        self.val = val                  # Object Attribute / Instance Attribute


o1 = Class1(10)
o2 = Class1(20)

print(o1.val)           # every object will have different values
print(o2.val)
