# class Class1:
#     attr1 = 11                  # class attribute

#     def display(self):          # instance method
#         print(f"display function called.")


# obj1 = Class1()

# print(obj1.attr1)
# obj1.display()
# print(Class1.attr1)     # we can access class attributes by class or object

# --------------------------------------------------------


class Class1:
    attr1 = 33                  # class attribute

    def __init__(self, val):
        self.val1 = val         # instance attribute

    def display(self):          # instance method
        print(f"display function called. val = {self.val1}")

    @classmethod                # @classmethod  decorator @
    def display2(cls):
        print(f"class display function called.")
        cls.attr1 = 22


obj1 = Class1(11)
obj2 = Class1(22)
print(obj1.attr1)           # 33
print(obj2.attr1)           # 33
print(obj1.val1)            # 11
print(obj2.val1)            # 22
print(Class1.attr1)         # 33


# # # print(Class1.val1) # error
# # obj1.display()
# # Class1.display2()
# # Class1.display3()
# # print(obj1.val1)
# # print(Class1.attr1)


#     @staticmethod               # static method
#     def display3():
#         print(f"static display function called.")
#         # attr1 = 202           # can't access class state
