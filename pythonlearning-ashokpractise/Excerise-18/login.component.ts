import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ToastrService } from 'ngx-toastr';
import { Router } from '@angular/router';
//import { SharingService } from '../sharing.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrl: './login.component.css',
})
export class LoginComponent {
  constructor(
    private formBuilder: FormBuilder,
    private toastr: ToastrService,
    private router: Router,
   // private sharingService: SharingService
  ) {}
  loginForm = this.formBuilder.group({
    userid: ['', Validators.required],
    passwd: ['', Validators.required],
  });

  onSubmit() {
    let uid = this.loginForm.value.userid;
    let pwd = this.loginForm.value.passwd;
    if (uid == 'admin' && pwd == 'admin') {
     // this.sharingService.isLoggedIn = true;
      this.toastr.success('Login Successful!');
      this.router.navigate(['/react2']);
    } else {
      //this.sharingService.isLoggedIn = false;
      this.toastr.error('Invalid Credentials!');
    }

    this.loginForm.reset();

    // console.log(this.loginForm.status);
  }}
