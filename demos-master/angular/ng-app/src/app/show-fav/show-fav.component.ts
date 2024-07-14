import { Component, OnInit } from '@angular/core';
import { FavService } from '../fav.service';
import { Emp } from '../Models/emp';

@Component({
  selector: 'app-show-fav',
  templateUrl: './show-fav.component.html',
  styleUrl: './show-fav.component.css',
})
export class ShowFavComponent implements OnInit {
  favs?: Emp[];
  totalSalary: number = 0;
  constructor(private favService: FavService) {}
  ngOnInit(): void {
    this.favs = this.favService.getFavs();
    this.totalSalary = this.favService.totalSalary;
    console.log(this.favs.length);
  }

  RemFav(e: Emp) {
    this.favService.remFav(e);
    this.favs = this.favService.getFavs();
    this.totalSalary = this.favService.totalSalary;
  }
}
