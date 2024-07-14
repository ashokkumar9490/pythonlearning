### Python - Exercise-7  

## Create A python program to practice Python OOP: Employee Hierarchy and Salary Calculation. This exercise involves creating a class hierarchy representing different employee types and their functionalities in a company.

Classes:

Employee: (Base Class)

Attributes:
name (str): Name of the employee.
experience (int): Years of experience.
Methods:
calculate_base_salary(self) (abstract): An abstract method to calculate the base salary (implemented by subclasses).
get_info(self): Returns a string representation of the employee (including name, experience, and salary).

Developer (Subclass of Employee)

Attributes:
programming_languages (list): List of programming languages the developer knows.
Methods:
calculate_base_salary(self): Override base class to implement a salary calculation specific to developers (e.g., based on experience and programming skills).

Manager (Subclass of Employee)

Attributes:
team_size (int): Number of employees the manager supervises.
Methods:
calculate_base_salary(self): Override base class to implement a salary calculation specific to managers (e.g., based on experience and team size).
Sample Code:


# Create employees and print their information
developer = Developer("Alice Developer", 5, ["Python", "Java"])
manager = Manager("Bob Manager", 8, 5)

print(developer.get_info())
print(manager.get_info())

Sample Output:

Employee: Alice Developer, Experience: 5 years, Salary: $62000.00
Employee: Bob Manager, Experience: 8 years, Salary: $91000.00
Explanation:

The base class Employee defines common attributes (name, experience) and methods (calculate_base_salary - abstract, get_info).

Subclasses Developer and Manager inherit from Employee and implement their specific salary calculation logic in the overridden calculate_base_salary method.

The get_info method in subclasses uses the calculated salary from calculate_base_salary to provide a detailed employee description.

Challenge:

Extend the class hierarchy to include more employee types (e.g., Salesperson, Analyst).
Modify the base class Employee to include a department attribute (e.g., IT, Marketing) and consider it while calculating salaries in subclasses.
Implement a method to award bonuses based on performance and incorporate it into the total salary calculation.
