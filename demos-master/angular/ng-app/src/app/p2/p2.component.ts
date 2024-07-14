import { Component } from '@angular/core';

@Component({
  selector: 'app-p2',
  templateUrl: './p2.component.html',
  styleUrl: './p2.component.css',
})
export class P2Component {
  msg: string = 'Message from Parent to Child Component';
  msg2: string = '';
}
