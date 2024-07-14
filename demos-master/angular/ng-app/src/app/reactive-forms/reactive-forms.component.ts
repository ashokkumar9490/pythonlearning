import { Component } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';

@Component({
  selector: 'app-reactive-forms',
  templateUrl: './reactive-forms.component.html',
  styleUrl: './reactive-forms.component.css',
})
export class ReactiveFormsComponent {
  formvalues = '';
  profileForm = new FormGroup({
    firstName: new FormControl('', Validators.required),
    lastName: new FormControl('', Validators.required),
  });
  onSubmit() {
    console.log(this.profileForm.value);
    this.formvalues =
      'you entered - ' +
      this.profileForm.value.firstName +
      ' ' +
      this.profileForm.value.lastName;
    // setvalue

    this.profileForm.setValue({
      firstName: 'John',
      lastName: 'Doe',
    });
  }
}
