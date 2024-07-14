import { Component, OnChanges, OnInit, SimpleChanges } from '@angular/core';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-welcome',
  templateUrl: './welcome.component.html',
  styleUrl: './welcome.component.css',
})
export class WelcomeComponent implements OnInit {
  constructor(private toastr: ToastrService) {}
  ngOnInit(): void {
    console.log('Welcome component - OnInit event');

    // this.toastr.success('Hello world!', 'Toastr fun!');
    // this.toastr.info('Hello world!', 'Toastr is working');
    // this.toastr.error('Hello world!', 'Some Error');
  }

  TryToastr() {
    //this.toastr.success('Hello world!', 'Toastr fun!');
  }
}
