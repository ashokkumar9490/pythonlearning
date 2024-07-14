import { Injectable } from '@angular/core';
import { ReplaySubject } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class SharingService {
  constructor() {}

  isLoggedIn: boolean = false; //check user
  isAdmin: boolean = false; //check admin

  public loggedin = new ReplaySubject<number>(0); // create a replay subject to store the value
  loggedin$ = this.loggedin.asObservable(); // create an observable to subscribe to

  doLogin() {
    // user login
    this.isLoggedIn = true;
    this.loggedin.next(1);
  }

  doAdminLogin() {
    // admin login
    this.isLoggedIn = true;
    this.isAdmin = true;
    this.loggedin.next(1);
  }

  doLogout() {
    this.isLoggedIn = false;
    this.isAdmin = false;
    this.loggedin.next(0);
  }
}
