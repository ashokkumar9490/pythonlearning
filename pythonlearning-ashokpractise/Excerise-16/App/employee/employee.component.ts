import { Component } from '@angular/core';

class Employee {
  id: number;
  name: string;
  salary: number;

  constructor(id: number, name: string, salary: number) {
    this.id = id;
    this.name = name;
    this.salary = salary;
  }
  getTax(): number {
    return this.salary * 0.1;

  }
  getPayablesalary(): number {
    return this.salary - this.getTax();
  }
}

@Component({
  selector: 'app-employee',
  templateUrl: './employee.component.html',
  styleUrl: './employee.component.css'
})
export class EmployeesComponent {

  employee: Employee[] = [new Employee(256283, "santosh", 50000),
  new Employee(256280, "aravind", 60000),
  new Employee(256290, "ashok", 55000),
  new Employee(256380, "naresh", 90000)]


}
