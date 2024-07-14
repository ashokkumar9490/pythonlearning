import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-react2',
  templateUrl: './react2.component.html',
  styleUrl: './react2.component.css',
})
export class React2Component {
  profileForm = this.formBuilder.group({
    firstName: ['', Validators.required],
    lastName: [''],
    address: this.formBuilder.group({
      street: [''],
      city: [''],
      state: [''],
      zip: [''],
    }),
  });

  constructor(private formBuilder: FormBuilder) {}

  updateProfile() {
    this.profileForm.patchValue({
      firstName: 'Nancy',
      address: {
        street: '123 Drew Street',
      },
    });
  }

  onSubmit() {
    console.warn(this.profileForm.value);
  }
}
