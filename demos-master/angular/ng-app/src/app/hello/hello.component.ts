import { Component, inject } from '@angular/core';
import { CalculatorService } from '../calculator.service';

@Component({
  selector: 'app-hello',
  templateUrl: './hello.component.html',
  styleUrl: './hello.component.css',
})
export class HelloComponent {
  constructor(private calc: CalculatorService) {}

  classname: string = 'text-danger'; // RED COLOR
  //calc2 = inject(CalculatorService);
  company: string = 'Google';
  weekDay: string = 'Mon';
  myName: string = 'Sharad';
  isDisabled = false;
  message: string = 'message will appear here...';
  salary: number = 24567;

  friendNames = ['Aman', 'Suresh', 'Neha', 'Jyothi'];
  myli = 'myli';
  SayHello() {
    this.message = 'Button Clicked...';
  }

  getIncrement() {
    return this.calc.add(this.salary, 5000);
  }
}
