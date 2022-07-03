var readline = require('readline-sync');

var Calculation = function(num1, num2, op) {
  this.x = parseInt(num1);
  this.y = parseInt(num2);
  this.op = op;

  this.result = function() {
    var x = this.x;
    var y = this.y;
    var op = this.op;

    if (op === "+") {
      var result = x + y;
    } else if (op === "-") {
      var result = x - y;
    } else if (op === "/") {
      var result = x / y;
    } else if (op === "*") {
      var result = x * y;
    } else if (op === "%") {
      var result = x % y;
    } else {
      var result = "Помилка!"
    }

    console.log("Результат: " + result);
  };
}

var num1 = readline.question("Enter first number: ");
var num2 = readline.question("Enter second number: ");
var op = readline.question("Enter operator: ");

var calc = new Calculation(num1, num2, op);

calc.result();