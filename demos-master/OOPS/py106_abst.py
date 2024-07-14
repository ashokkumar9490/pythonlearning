# Python program showing
# abstract base class work
from abc import ABC, abstractmethod


class Polygon(ABC):

    @abstractmethod
    def noofsides(self):
        pass


class Triangle(Polygon):
    # pass
    # Can't instantiate abstract class Triangle
    # without an implementation for abstract method 'noofsides

    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")


class Pentagon(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 5 sides")


# p = Polygon()  # error  can't instantiate

O = Triangle()

R = Triangle()
R.noofsides()

p = Pentagon()
p.noofsides()

# K = Polygon()
# K.noofsides()
