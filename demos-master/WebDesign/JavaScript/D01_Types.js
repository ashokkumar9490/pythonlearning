// n n b b s s u o
// number null bool bigint string symbol undef object

let a = 10;
let b = null;
let c = true;
let d = BigInt(100);
let e = "Sharad";
let g = undefined;

console.log(typeof a);
console.log(typeof b);
console.log(b === null);
console.log(typeof c);
console.log(typeof d);
console.log(typeof e);
console.log(typeof g);

let person = {
  id: 1,
  name: "p1",
  city: "Pune",
  pin: null,
};
console.log(person);
console.log(person.name);
console.log(person.pin);
console.log(person.country); // undef
person["country"] = "India";
console.log(person);
console.log(person.country);
console.log(person["country"]);
