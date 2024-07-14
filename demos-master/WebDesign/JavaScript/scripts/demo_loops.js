function demo_for1() {
  let str = "";
  for (let index = 1; index < 11; index++) {
    str += String(index) + " ";
  }
  console.log(str);
}

function demo_forOf() {
  let arr = [11, 66, 55, 33, 99];
  for (const item of arr) {
    console.log(item);
  }
}
let x = 10;
x = 20;
const y = 22;
// y = 33; // Assignment to constant variable not allowed
// console.log(y);

function demo_for2() {
  let arr = [11, 66, 55, 33, 99];
  for (let i = 0; i < arr.length; i++) {
    console.log(arr[i]);
  }
}

function demo_while() {
  let x = 1;
  while (x < 11) {
    console.log(x);
    x++;
  }
}

function demo_foreach() {
  arr = [3, 4, 8, 9, 6];
  arr.forEach((item, index) => {
    // fat arrow
    console.log(`${index + 1} - ${item}`); // callback function
  });
}

demo_foreach();

// let x = 10;
// console.log(`X = ${x}`); // interpolation of values and text

// let arr = [11, 66, 55, 33, 99];
// console.log(arr.join()); // default , separator
