class Class1:
    def __init__(self):
        self.__name = "Sharad"      # private double _
        self._city = "Delhi"        # protected single _
        self.age = 33               # public


obj1 = Class1()
print(obj1.__name)      # error
print(obj1.age)
