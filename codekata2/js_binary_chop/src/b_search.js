var BinarySearch = (function() {

  var binaryChop = function (target, intArray, balance) {
    //if balance undefined set to 0
    balance = typeof balance !== 'undefined' ? balance : 0;

    //get midpoint of int array, round down if uneven
    var mid = Math.floor((intArray.length - 1) / 2);

    //if target is mid return index of element
    if (target === intArray[mid]) {
      return mid + balance;
    }
    //if target not found or intArray is empty return -1
    else if (intArray.length === 1 || intArray.length === 0) {
      return -1;
    }
    
    //target is smaller than mid
    if (target < intArray[mid]) {
      index = binaryChop(target, intArray.slice(0, mid));
    }
    //target is larger than mid
    else{
      index = binaryChop(
          target, intArray.slice(mid+1, intArray.length), balance+mid+1
      );
    }
    return index;
  }; 

  return {
    binaryChop: binaryChop
  };

}());
