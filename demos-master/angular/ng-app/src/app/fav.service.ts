import { Injectable } from '@angular/core';
import { Emp } from './Models/emp';
import { ReplaySubject } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class FavService {
  emps: Emp[] = [];

  totalSalary: number = 0;

  private favCount = new ReplaySubject<number>(0);
  favCount$: any = this.favCount.asObservable();

  constructor() {
    this.favCount.next(this.emps.length);
  }

  addFav(emp: Emp) {
    let e = this.emps?.find((p) => p.id === emp.id);
    if (!e) {
      this.emps.push(emp);
      this.totalSalary += Number(emp.salary);
      this.favCount.next(this.emps.length);
      return true;
    } else {
      return false;
    }
  }

  remFav(emp: Emp) {
    this.emps = this.emps.filter(function (obj) {
      return obj.id !== emp.id;
    });
    this.totalSalary -= emp.salary;
    this.favCount.next(this.emps.length);
  }

  public getFavs() {
    return this.emps;
  }
}
