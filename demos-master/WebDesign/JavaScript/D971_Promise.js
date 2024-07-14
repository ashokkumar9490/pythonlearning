function myDisplayerOK(some) {
  console.log("OK------------------" + some);
}
function myDisplayerError(some) {
  console.log("Error ----------------------" + some);
}

let myPromise = new Promise(function (myResolve, myReject) {
  let x = 2;

  // The producing code (this may take some time)

  if (x == 1) {
    myResolve("OK");
  } else {
    myReject("Error");
  }
});

myPromise.then(
  function (value) {
    myDisplayerOK(value);
  },
  function (error) {
    myDisplayerError(error);
  }
);
