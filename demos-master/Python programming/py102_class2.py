class Employee:
    dept = "Accounts"

    def __init__(self, id,  name, age, city):
        self.id = id
        self.name = name
        self.age = age
        self.city = city
        self.salary = 10000


emp1 = Employee(id=1, name="Suman", age=21,  city="Hyderabad")
print(emp1)
print(emp1.id)
print(emp1.name)
print(emp1.dept)

if __name__ == "__main__":
    print("Starting with Class Demo")
