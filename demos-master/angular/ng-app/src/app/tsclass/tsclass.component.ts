import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-tsclass',
  templateUrl: './tsclass.component.html',
  styleUrl: './tsclass.component.css',
})
export class TsclassComponent implements OnInit {
  s1: Student = new Student();
  ngOnInit(): void {
    console.log(this.s1.sname); // GETTER
    this.s1.sname = 'Jane Dev'; // SETTER
    console.log(this.s1.studentInfo);
  }
}

class Student {
  private name: string = 'John Doe';
  private semester: number = 1;
  private course: string = 'Computer Science';

  get sname(): string {
    // getter property
    return this.name;
  }
  set sname(name: string) {
    // setter property
    this.name = name;
  }

  get studentInfo(): string {
    return `Name: ${this.name}, Semester: ${this.semester}, Course: ${this.course}`;
  }
}
