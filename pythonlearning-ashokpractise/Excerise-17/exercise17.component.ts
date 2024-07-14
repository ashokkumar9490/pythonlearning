import { Component } from '@angular/core';
 
@Component({
  selector: 'app-exercise17',
  templateUrl: './exercise17.component.html',
  styleUrls: ['./exercise17.component.css']
})
export class Exercise17Component {
  products = [
    { name: 'Laptop', price: 100000, category: 'Electronics' },
    { name: 'Shirt', price: 1200, category: 'Clothing' },
    { name: 'Headphones', price: 750, category: 'Electronics' },
    { name: 'Dress', price: 4000, category: 'Clothing' },
    { name: 'Coffee Maker', price: 1500, category: 'Home' },
  ];
 
  selectedCategory: string = '';
 
  get filteredProducts() {
    if (!this.selectedCategory) {
      return this.products;
    }
    return this.products.filter(product => product.category === this.selectedCategory);
  }
}