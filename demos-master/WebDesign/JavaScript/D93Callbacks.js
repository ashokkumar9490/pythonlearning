// function myFirst() {
//   myDisplayer("Hello");
// }

// function mySecond() {
//   myDisplayer("Goodbye");
// }

// myFirst();
// mySecond();

// //-----JavaScript functions are executed in the sequence-------------------------------------------------

// // Suppose you want to do a calculation, and then display the result

// function myDisplayer(some) {
//   document.getElementById("demo").innerHTML = some;
// }

// function myCalculator(num1, num2) {
//   let sum = num1 + num2;
//   return sum;
// }

// let result = myCalculator(5, 5);
// myDisplayer(result);

// //----------- you have to call two functions to display the result

// function myDisplayer(some) {
//   document.getElementById("demo").innerHTML = some;
// }

// function myCalculator(num1, num2) {
//   let sum = num1 + num2;
//   myDisplayer(sum);
// }

// myCalculator(5, 5);

//-----------you cannot prevent the calculator function from displaying

//------------------it is time to bring in a callback----------------------------

// function myDisplayer(some) {
//   document.getElementById("demo").innerHTML = some;
// }

// function myCalculator(num1, num2, myCallback) {
//   let sum = num1 + num2;
//   myCallback(sum);
// }

// myCalculator(5, 5, myDisplayer);

// myCalculator(5, 5); // may avoid calling display

// ------------myDisplayer is a called a callback function
// A callback is a function passed as an argument to another function

// setTimeout will run function after defined time
// setTimeout(function () {
//   console.log("Hello");
// }, 3000); // 3000 millisonds - 3 seconds

// will run repeatedly after every defined time
setInterval(() => {
  console.log("Hello again");
}, 3000);
// function myFunction(value) {
//   console.log(value);
// }
