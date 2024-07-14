// Inheritance example
class person {
  constructor(name) {
    this.name = name;
  }
  // method to return the string
  toString() {
    return `Name of person: ${this.name}`;
  }
  Show() {
    console.log("Show in person");
  }
}
class student extends person {
  constructor(name, id) {
    // super keyword for calling the above
    // class constructor
    super(name);
    this.id = id;
  }
  toString() {
    return `${super.toString()}, Student ID: ${this.id}`;
  }
  Display() {
    super.Show();
  }
}
let student1 = new student("Mukul", 22);
console.log(student1.toString());
console.log(student1);
//student1.Display();
