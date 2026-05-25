var lowestScore = 100;
var highestScore = 0;

var average = 0;
var totalScore = 0;
var totalTests = 0;

var validate = true

do {
    var number = parseInt(prompt("Add a test score (-1 to stop) : "));
    if (number >= 0 && number <= 100) {
        totalTests ++;
        totalScore += number;
        if (number < lowestScore) {
            lowestScore = number;
        }
        if (number > highestScore) {
            highestScore = number;
        }
        average = totalScore/totalTests
    }
    else {
        if (number != -1) {
            document.write("Refresh this page and enter a number between 1 and 100.")
            break;
        }
    }
} while (number != -1);

if (number >= 0 && number <= 100 || number == -1 ) {
    document.write("The average score was : " + String(average) + "<br>")
    document.write("The sum of all test scores was : " + String(totalScore) + "<br>")
    document.write("The lowest score was : " + String(lowestScore) + "<br>")
    document.write("The highest score was : " + String(highestScore) + "<br>")
}






