# create class employee with properties id, name, department, salary
class Employee:
    def __init__(self, id, name, department, salary):
        self.id = id
        self.name = name
        self.department = department
        self.salary = salary

    def __str__(self):
        return f"** ID: {self.id}, Name: {self.name}, Department: {self.department}, Salary: {self.salary}"

    def __repr__(self):
        return f"Employee('{self.id}', '{self.name}', '{self.department}', '{self.salary}')"


emp1 = Employee(1, "Mahesh", "IT", 50000)
print(emp1)
print(emp1.__repr__())
emp2 = eval(repr(emp1))
print(emp2)
