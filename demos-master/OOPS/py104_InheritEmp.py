from abc import ABC, abstractmethod


class Employee(ABC):

    def __init__(self, name, salary, experience):
        self.name = name
        self.salary = salary
        self.experience = experience

    @abstractmethod
    def get_info(self):
        return f"Employee: {self.name}, Experience: {self.experience} years, Salary: ${self.salary}"


class Developer(Employee):
    def __init__(self, name, salary, experience, programming_languages):
        super().__init__(name, salary, experience)
        self.programming_languages = programming_languages

    def get_info(self):
        return super().get_info() + ", Languages Known - " + str(self.programming_languages)


class Manager(Employee):
    def __init__(self, name, salary, experience, team_size):
        super().__init__(name, salary, experience)
        self.team_size = team_size

    def get_info(self):
        return super().get_info() + ", Team Size - " + str(self.team_size)


# Create employees and print their information
developer = Developer("Alice Developer", 45678, 5, ["Python", "Java"])
manager = Manager("Bob Manager", 45678, 8, 5)

print(developer.get_info())
print(manager.get_info())
emp1 = Employee("Emp1", 34566, 5)
print(emp1.get_info())
