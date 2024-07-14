class Animal:   # parent / super / base
    def __init__(self, name):
        self.name = name
        print("Animal object created")

    def speak(self):
        print("Animal speaks")

    def __str__(self):
        return f"Animal name is {self.name}"

    def eat(self):
        print("Animal eats")


class Dog(Animal):      # child / derived
    def __init__(self, name):
        super().__init__(name)
        print("Dog object created")

    def speak(self):                        # overriding of methods
        print("Dog barks")


dog1 = Dog("Tommy")
print(dog1)
dog1.speak()
dog1.eat()

animal1 = Animal("Pet")


# class A(object):
#     def __init__(self):
#         print('A')
#         super().__init__()


# class B(A):
#     def __init__(self):
#         super().__init__()
#         print('B')


# o1 = A()
# o2 = B()
