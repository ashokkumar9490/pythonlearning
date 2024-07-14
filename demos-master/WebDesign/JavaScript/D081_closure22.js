function GetCount() {
  let counter = 0;
  // nested function
  function GetCounter() {
    counter += 1;
    return counter;
  }
  return GetCounter;
}

let f = GetCount();

console.log(f());
console.log(f());
console.log(f());

// This is called a JavaScript closure.
// It makes it possible for a function to have "private" variables.
// variable counter can not be used from outside
