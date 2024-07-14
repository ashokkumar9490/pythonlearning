import { Component } from '@angular/core';
import { FormControl } from '@angular/forms';

@Component({
  selector: 'app-react1',
  templateUrl: './react1.component.html',
  styleUrl: './react1.component.css',
})
export class React1Component {
  // step 1
  colorControl = new FormControl('red');
  updateName() {
    console.log('current value - ', this.colorControl.value);
    // change the value using setValue
    this.colorControl.setValue('yellow');
  }
}
