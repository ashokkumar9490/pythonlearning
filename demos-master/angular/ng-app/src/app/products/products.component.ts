import { Component } from '@angular/core';

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrl: './products.component.css',
})
export class ProductsComponent {
  products = [
    { name: 'Laptop', price: 1200, category: 'Electronics' },
    { name: 'Shirt', price: 25, category: 'Clothing' },
    { name: 'Headphones', price: 75, category: 'Electronics' },
    { name: 'Dress', price: 50, category: 'Clothing' },
    { name: 'Coffee Maker', price: 80, category: 'Home' },
  ];

  selectedCategory: string = '';

  get filteredProducts(): Product[] {
    if (this.selectedCategory === '') {
      return this.products; // Return all products if no category is selected
    }
    return this.products.filter(
      (product) => product.category === this.selectedCategory
    );
  }
}

class Product {
  name: string = '';
  price: number = 0;
  category: string = '';
}
