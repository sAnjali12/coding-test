function sum(num){
    var sumNumber = num+20
    return sumNumber
}

function multiply(callBack){
    var multiNumber = 34*callBack;
    return multiNumber;

}
var result = multiply(sum(24));
console.log(result)