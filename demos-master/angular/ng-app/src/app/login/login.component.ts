import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ToastrService } from 'ngx-toastr';
import { Router } from '@angular/router';
import { ProfileService } from '../profile.service';
import { SharingService } from '../sharing.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrl: './login.component.css',
})
export class LoginComponent {
  token: any = 'Invalid';

  userdata: any = [];
  userid: any = '';
  userType: any = 'userType';

  constructor(
    private formBuilder: FormBuilder,
    private toastr: ToastrService,
    private router: Router,
    private profileService: ProfileService,
    private sharingService: SharingService
  ) {}

  loginForm = this.formBuilder.group({
    userid: ['', Validators.required],
    passwd: ['', Validators.required],
  });

  fetchProfile() {
    if (this.token === 'Invalid') {
      console.log('Invalid Credentials');
    } else {
      this.token = localStorage.getItem('token');
      this.profileService.fetchProfile(this.token).then((data) => {
        console.log(data);

        this.userdata = data;

        let user = data.filter((user: any) => user.email === this.userid);
        console.log(user);

        this.userType = user[0].is_staff ? 'admin' : 'user';
      });
    }
  }

  fetchProfiles() {
    this.profileService.fetchProfiles().then((data) => {
      console.log(data);
      this.userdata = data.users;
    });
  }

  // create a method to handle fetchToken method and store the token
  login(name: string, password: string) {
    this.profileService
      .fetchToken(name, password)
      .then((data) => {
        console.log('logging fetch token -  ' + data.token);
        // if response data does not contain token
        if (data.token == undefined) {
          console.log('Invalid Credentials for getting token');
          this.sharingService.isAdmin = false;
          this.toastr.error('Invalid Credentials!');
        } else {
          // if token is available in response
          this.sharingService.doAdminLogin();
          this.toastr.success('Admin Login Successful!');
          this.token = data.token;
          localStorage.setItem('token', data.token);
        }
      })
      .then(() => this.fetchProfile());
  }

  onSubmit() {
    console.log('Submitting Login info');

    let uid: string = this.loginForm.value.userid || '';
    let pwd: string = this.loginForm.value.passwd || '';

    this.userid = uid;

    console.log('Submit Login data ', uid, pwd);

    this.login(uid, pwd);
    // if (uid == 'user' && pwd == 'user') {
    //   //this.sharingService.doLogin();
    //   //this.toastr.success('User Login Successful!');
    //   this.router.navigate(['/hello']);
    // } else if (uid == 'admin' && pwd == 'admin') {
    //   //this.sharingService.doAdminLogin();
    //   //this.toastr.success('Admin Login Successful!');
    //   //this.router.navigate(['/welcome']);
    // } else {
    //   //this.sharingService.isLoggedIn = false;
    //   //this.sharingService.isAdmin = false;
    //   //this.toastr.error('Invalid Credentials!');
    // }

    this.loginForm.reset();

    // console.log(this.loginForm.status);
  }
}
