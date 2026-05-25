// Ask user for data 
var number = prompt("Please enter any natural number:")

// Validate data
if (parseInt(number) < 1 || number % 1 != 0) {
    document.write("You did not enter a natural number.")
}

//Creates new varible
factorial = 1

//Function to find factorial
var solveSequence = function(num){
    if (parseInt(num) == 1) {
        document.write(" 1 = ")
        return factorial;
    }
    else {
        document.write(num + " x ")
        factorial = factorial * num
        return solveSequence(num-1)
    }
}

//Writes final factorial
var finalFactorial = solveSequence(number)
document.write(finalFactorial)