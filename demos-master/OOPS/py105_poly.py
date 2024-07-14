class Animal:
    def __init__(self, name):
        self.name = name
        print("Animal object created")

    def speak(self):
        print("Animal speaks")

    def __str__(self):
        return f"Animal name is {self.name}"

    def eat(self):
        print("Animal eats")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        print("Dog object created")

    def speak(self):
        print("Dog barks")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        print("Cat object created")

    def speak(self):
        print("Cat meows")


dog1 = Dog("Tommy")
# print(dog1)
# dog1.speak()
# dog1.eat()

cat1 = Cat("Kitty")
# print(cat1)
# cat1.speak()
# cat1.eat()

mypets = [dog1, cat1]       # collection List

for obj in mypets:
    obj.speak()         # many forms - overriding
