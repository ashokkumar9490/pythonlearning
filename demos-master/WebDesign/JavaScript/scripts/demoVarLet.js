console.log(x); // undefined

var x = 10;
let y = 10;

function checkScope() {
  console.log(x);
  console.log(y);
  let z = 111;

  if (true) {
    let c = 222;
    var c2 = 33;
  }

  // console.log(c);
  console.log(c2);
  // console.log(c); // outside defined scope - if block
}

//console.log(c2);
// console.log(z); // : z is not defined in this scope

var x = "Sharad"; // var variables can declared again

// let y = "Sharad"; // Cannot redeclare block-scoped variable 'y'

y = "Sharad";

console.log(x);
checkScope();
