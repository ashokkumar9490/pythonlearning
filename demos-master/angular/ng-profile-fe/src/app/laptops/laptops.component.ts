import { Component } from '@angular/core';

@Component({
  selector: 'app-laptops',
  templateUrl: './laptops.component.html',
  styleUrl: './laptops.component.css',
})
export class LaptopsComponent {
  laptops: any = [
    {
      name: 'Dell',
      price: 50000,
      description: 'RAM-32GB,SDD-2TB',
    },
    {
      name: 'HP',
      price: 60000,
      description: 'RAM-16GB,SDD-1TB',
    },
    {
      name: 'Lenovo',
      price: 40000,
      description: 'RAM-32GB,SDD-2TB',
    },
  ];
}
