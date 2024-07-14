import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-parent',
  templateUrl: './parent.component.html',
  styleUrls: ['./parent.component.css'],
})
export class ParentComponent implements OnInit {
  msg: string = 'How are you? Child...'; // will be passed to child
  msg2: string = ''; // to get value from child component

  constructor() {}

  ngOnInit(): void {}

  getMessage(evt: any) {
    this.msg2 = evt;
  }
}
