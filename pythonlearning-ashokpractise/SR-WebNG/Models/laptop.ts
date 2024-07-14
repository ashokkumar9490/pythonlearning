export class Lap {
  id: number = 0;
  model: string = '';
  company: string = '';
  price: number = 0;
  constructor(id: number, model: string, company: string, price: number) {
    this.id = id;
    this.model = model;
    this.company = company;
    this.price = price;
  }
}
