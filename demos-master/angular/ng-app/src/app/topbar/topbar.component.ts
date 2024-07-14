import { Component, OnInit } from '@angular/core';
import { SharingService } from '../sharing.service';
import { FavService } from '../fav.service';

@Component({
  selector: 'app-topbar',
  templateUrl: './topbar.component.html',
  styleUrl: './topbar.component.css',
})
export class TopbarComponent implements OnInit {
  isLogged = false;
  loggedin$: any;
  favcount$: any;

  constructor(
    private service: SharingService,
    private favService: FavService
  ) {}

  ngOnInit(): void {
    this.isLogged = this.service.isLoggedIn;
    this.loggedin$ = this.service.loggedin$; // subscribe to the observable
    this.favcount$ = this.favService.favCount$;
    console.log(this.isLogged);
  }
}
