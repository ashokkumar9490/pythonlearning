from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, name, experience, salary):
        self.name = name
        self.experience = experience
        self.salary = salary
    def get_info(self):
        return f"Employee : {self.name} with {self.experience} years of experience , salary is $ {self.salary}"
 
class Developer(Employee):
    
    def __init__(self, name, experience, salary, programming_languages):
        super().__init__(name, experience, salary)
        self.programming_languages = programming_languages
 
    def get_info(self):
        return f"{super().get_info()}{self.programming_languages}"
    @abstractmethod
    def calculate_base_salary(self):
        pass
 
class Manager(Employee):
    def __init__(self, name, experience, salary, team_size):
        super().__init__(name, experience, salary)
        self.team_size = team_size
    def get_info(self):
        return f"{super().get_info()} team size :{self.team_size})"
 
if __name__ == "__main__":
    developer = Developer("Alice", 5, 60000, ["Python", "Java"])
    print(developer.get_info())
    manager = Manager("Bob", 8, 112000, 5)
    print(manager.get_info())