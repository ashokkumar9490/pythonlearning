import { Component, OnInit } from '@angular/core';
import { ProfileService } from '../profile.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrl: './profile.component.css',
})
export class ProfileComponent implements OnInit {
  token: any = '';

  constructor(private loginService: ProfileService) {}

  ngOnInit() {
    this.login('sharad@gmail.com', 'Sharad@123');
  }

  // pass form data to login function on submit event

  fetchProfile() {
    this.token = localStorage.getItem('token');
    this.loginService.fetchProfile(this.token).then((data) => {
      console.log(data);
    });
  }

  // create a method to handle fetchToken method and store the token
  login(name: string, password: string) {
    this.loginService
      .fetchToken(name, password)
      .then((data) => {
        console.log(data);
        localStorage.setItem('token', data.token);
      })
      .then(() => this.fetchProfile());
  }
}
