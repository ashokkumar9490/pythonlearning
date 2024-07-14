// Defining class using es6
class Vehicle {
  #year = 2001; // private property

  // properties
  name;
  maker;
  engine;

  constructor(name, maker, engine) {
    this.name = name;
    this.maker = maker;
    this.engine = engine;
    this.year = this.#year + 5;
  }
  getDetails() {
    return `The name of the bike is ${this.name}. Year(private) is ${
      this.#year
    } Year(public) is ${this.year}`;
  }
}
// Making object with the help of the constructor
let bike1 = new Vehicle("Hayabusa", "Suzuki", "1340cc");
let bike2 = new Vehicle("Ninja", "Kawasaki", "998cc");

console.log(bike1.name); // Hayabusa
console.log(bike2.maker); // Kawasaki
console.log(bike2.year);
console.log(bike1.getDetails());

// https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Classes_in_JavaScript
