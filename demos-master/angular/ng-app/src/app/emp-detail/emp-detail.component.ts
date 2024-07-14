import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Route } from '@angular/router';
import { Emp } from '../Models/emp';
import { EmpsService } from '../emps.service';
import { FavService } from '../fav.service';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-emp-detail',
  templateUrl: 'emp-detail.component.html',
  styleUrl: './emp-detail.component.css',
})
export class EmpDetailComponent implements OnInit {
  edet?: Emp;
  constructor(
    private route: ActivatedRoute,
    private empsService: EmpsService,
    private favService: FavService,
    private toastr: ToastrService
  ) {}
  ngOnInit(): void {
    const routeParams = this.route.snapshot.paramMap;
    const idFromRoute = Number(routeParams.get('Id'));
    console.log(idFromRoute);
    this.getEmpById(idFromRoute);
  }

  getEmpById(id: number) {
    this.empsService.getEmpById(id).then((data) => {
      console.log(data);
      this.edet = data;
      console.log(this.edet);
    });
  }
  addFav(emp: Emp) {
    console.log('Adding Fav ');

    let isAdded: Boolean = this.favService.addFav(emp);
    if (isAdded) {
      this.toastr.success('Fav Added!');
    } else {
      this.toastr.error('Fav Already Existing!');
    }
  }
}
