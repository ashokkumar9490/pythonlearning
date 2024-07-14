// map - map() creates a new array from calling a function for every array element
// map() does not change the original array.
const numbers = [4, 9, 16, 25];

// const newArr = numbers.map(Math.sqrt);
// console.log(newArr.toString());

// const newArr2 = numbers.map(myFunc);
// console.log(newArr2.toString());

// function myFunc(num) {
//   return num * 10;
// }

// // anonymous function
// const newArr3 = numbers.map(function (num) {
//   return num * 10;
// });
// console.log(newArr3.toString());

// const newArr4 = numbers.map((num) => num * 10); // fat arrow functions
// console.log(newArr4.toString());

// var arr1 = [20, 5.2, -120, 100, 30, 0];   // string sorting
// arr1.sort();
// console.log(arr1.toString());

/* Logic: 
   20 - (5.2) = +ve => 5.2 would be placed before 20,
   20 - (-120) = +ve => -120 would be placed before 20,
   20 - (100) = -ve => 100 would be placed after 20,
   20 - (30) = -ve => 30 would be placed after 20,
   20 - (0) = +ve => 0 would be placed before 20,
   Similarly for every element, we check 
   and place them accordingly in iterations.
*/

var arr1 = [20, 5.2, -120, 100, 30, 0];
arr1.sort((a, b) => a - b);
console.log(arr1.toString());

// var arr = [100, 22, 333, 23];
// // arr.sort(function (a, b) {
// //   return a - b;
// // });
// arr.sort((a, b) => a - b);
// console.log(arr.toString());
