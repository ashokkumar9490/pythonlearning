// counter = 0;
// function GetCount() {
//   counter += 1;
//   return counter;
// }

// let f = GetCount();
// console.log(f);
// f = GetCount();
// console.log(f);

// counter = 10;
// f = GetCount();
// console.log(f);

// problem is counter variable could be updated by any statement in code, not only by GetCount method

// OR

// if we make the counter variable local to function, it is initialized to 0 everytime we call the function
// A JavaScript inner function can solve this.
// closure - Maintaining state between each function call
// and to use private variables

// function GetCount() {
//   let counter = 0;
//   counter += 1;
//   return counter;
// }

// let f = GetCount();
// console.log(f);
// f = GetCount();
// console.log(f);

// counter = 10;
// f = GetCount();
// console.log(f);
