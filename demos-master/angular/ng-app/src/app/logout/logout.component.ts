import { Component, OnInit } from '@angular/core';
import { SharingService } from '../sharing.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-logout',
  templateUrl: './logout.component.html',
  styleUrl: './logout.component.css',
})
export class LogoutComponent implements OnInit {
  constructor(private sharingService: SharingService, private router: Router) {}
  status: boolean = false;

  ngOnInit() {
    this.status = this.sharingService.isLoggedIn;
  }

  onLogout() {
    this.sharingService.doLogout();
    this.status = false;
    this.router.navigate(['/']);
  }
  onCancel() {
    this.status = true;
    this.router.navigate(['/emps']);
  }
}
