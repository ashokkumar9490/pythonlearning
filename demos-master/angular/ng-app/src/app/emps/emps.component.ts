import { Component, OnInit } from '@angular/core';
import { EmpsService } from '../emps.service';
// import emp class
import { Emp } from '../Models/emp';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-emps',
  templateUrl: './emps.component.html',
  styleUrl: './emps.component.css',
})
export class EmpsComponent implements OnInit {
  emps: any;
  start: boolean = true;
  error: string = '';
  countMarked: number = 0;

  empForm = this.fb.group({
    id: [''],
    name: [''],
    salary: [''],
    image: [''],
  });

  ngOnInit() {
    this.getEmpsFromService();
  }

  constructor(private empsService: EmpsService, private fb: FormBuilder) {}

  // get all employees
  getEmpsFromService() {
    this.empsService
      .getEmps()
      .then((data) => {
        console.log(data);
        this.emps = data;
        this.start = false;
      })
      .catch((err) => {
        console.log(err);
        this.error = 'Error fetching data.. Check server is running or not..';
      });
  }

  onSubmit() {
    let id = Number(this.empForm.value.id);
    let name = this.empForm.value.name || '';
    let salary = Number(this.empForm.value.salary);
    let image = this.empForm.value.image || '';

    console.log(id, name, salary, image);

    this.addEmp(new Emp(id, name, salary, image));
    this.empForm.reset();
  }

  addEmp(emp: Emp) {
    this.empsService.addEmp(emp).then(() => {
      this.getEmpsFromService();
    });
  }

  DelEmp(emp: Emp) {
    this.empsService.deleteEmp(emp.id).then(() => {
      this.getEmpsFromService();
    });
    this.countMarked = 0;
  }
  MarkEmp(emp: Emp) {
    this.emps.map((e: any) => {
      if (e.id == emp.id && !e.name.endsWith('*')) {
        e.name = e.name + '*';
        this.countMarked += 1;
      }
    });
  }
}
