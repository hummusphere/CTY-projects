// loop to obtain and store data
integers = [];

for (var i = 0; i < 10; i++) {
    var number = (prompt("Enter an whole number : "))
    if (number % 1 == 0 ) {
        if (number >= 0) {
            integers.push(number)
        } else {
            alert("You did not enter an whole number.")
            break;
        }
    }
    else {
        alert("You did not enter an whole number.")
        break;
    }
    
}

//Solves for the averge
currentSum = 0

var findAverage = function(num, currentSum) {
    currentSum += parseInt(num);
    return currentSum
}

for (var i = 0; i < integers.length; i++) {
    currentSum = findAverage(integers[i], currentSum)
}

average = currentSum/(integers.length)


//Solves for the maximum value
currentMax = 0

var findMaximum = function(num, currentMax) {
    if (parseInt(num) > currentMax) {
        return parseInt(num)
    }
    else {
        return currentMax
    }
}

for (var i = 0; i < integers.length; i++) {
    currentMax = findMaximum(integers[i], currentMax)
}


// Solves for the current minimum value
var maximum = currentMax

currentMin = maximum

var findMinimum = function(num, currentMin) {
    if (parseInt(num) < currentMin) {
        return parseInt(num)
    }
    else {
        return currentMin
    }
}

for (var i = 0; i < integers.length; i++) {
    currentMin = findMinimum(integers[i], currentMin)
}

minimum = currentMin

//Solves for the range value

var findRange = function(maximum, minimum) {
    range = maximum - minimum
    return range;
}

var range = findRange(maximum, minimum)

//Writes final results
document.write("Your numbers were : " + String(integers) + "<br>")
document.write("The average was : " + String(average) + "<br>")
document.write("The maximum value was : " + String(maximum) + "<br>")
document.write("The minimum value was : " + String(minimum) + "<br>")
document.write("The range was : " + String(range) + "<br>")