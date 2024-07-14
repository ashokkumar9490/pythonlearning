import { Component } from '@angular/core';
import { LaptopService } from '../laptop.service';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Lap } from '../Models/laptop';
//import { ToastrService } from 'ngx-toaster';

@Component({
  selector: 'app-laptop',
  templateUrl: './laptop.component.html',
  styleUrl: './laptop.component.css',
})
export class LaptopComponent {
  laps?: any;

  lap?: any;

  count: number = 0;

  error: string = 'hjgvjdc';

  ngOnInit() {
    this.getLapsFromService();
  }

  //injecting laptop service
  constructor(private lapService: LaptopService, private fb: FormBuilder) {}
  // private toastService:ToastrService){}

  //getting laptop data  from service
  getLapsFromService() {
    this.lapService
      .getLaps()
      .then((data) => {
        console.log(data);
        this.laps = data;
      })
      .catch((err) => {
        console.log(err);
        this.error = 'Error Fetching Data..Check if service is running';
      });
  }

  //creates a reactive form fields using formgroup and formbuilder
  loginForm = this.fb.group({
    id: ['', Validators.required],
    model: [''],
    company: [''],
    price: [''],
  });

  onSubmit() {
    console.warn(this.loginForm.value);
    let id = Number(this.loginForm.value.id);
    let model = this.loginForm.value.model || ' ';
    let company = this.loginForm.value.company || ' ';
    let price = Number(this.loginForm.value.price);

    console.log(id, model, company, price);
    this.addLapsFromService(new Lap(id, model, company, price));
  }

  addLapsFromService(lap: Lap) {
    //calling addLaps() from laptop service
    this.lapService.addLaps(lap).then(() => {
      this.getLapsFromService();
    });
  }

  delRow(lap: Lap, index: number): void {
    if (this.laps) {
      // to check emps have some products
      if (this.laps[index].model.endsWith('*')) {
        this.count -= 1; // Decrease the count if the employee is marked
      }
      this.lapService.delLap(lap);
      this.laps.splice(index, 1); // Update the local array to reflect the removal
    }
  }

  addMark(lap: Lap): void {
    if (this.laps) {
      // to check laps have some products
      let lapIndex = this.laps.findIndex(
        (l: { id: number }) => l.id === lap.id
      );
      if (this.laps[lapIndex].model.endsWith('*')) {
        //alert("already marked as *")
        //this.toastService.error("Row already marked as *")
      } else {
        this.laps[lapIndex].model += '*';
        this.count += 1;
      }
    }
  }
}
