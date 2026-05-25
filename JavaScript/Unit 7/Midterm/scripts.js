var incorrectQuestions = [];
var questions = [
    Brazil = {question: "This country has 27 stars on its flag.", answer: "Brazil"},
    Canada = {question: "This country produces alot of maple syrup.", answer: "Canada"},
    Chile = {question: "This country is the most narrow country on Earth.", answer: "Chile"},
    China = {question: "This country contains the Yellow and Yangtze river.", answer: "China"},
    Egypt = {question: "Many great pyramids were built in this country.", answer: "Egypt"},
    Germany = {question: "This country lost two world wars ...", answer: "Germany"},
    Greece = {question: "This country had the first democracy in the world.", answer: "Greece"},
    India = {question: "The Taj Mahal was built in this country.", answer: "India"},
    Italy = {question: "The capital this country was the center of the Roman Empire.", answer: "Italy"},
    Japan = {question: "This country has the largest capital in the world.", answer: "Japan"},
    Mexico = {question: "This country uses pesos as its currency.", answer: "Mexico"},
    Philippines = {question: "This country is home to the largest underground river.", answer: "Philippines"},
    Russia = {question: "This country is currently fighting a war in Ukraine.", answer: "Russia"},
    Saudi_Arabia = {question: "This country is a big exporter of oil.", answer: "Saudi Arabia"},
    South_Africa = {question: "The worlds largest crater is visible in this country.", answer: "South Africa"},
    South_Korea = {question: "In this country, kids are one year old when they are born.", answer: "South Korea"},
    Spain = {question: "This country used to control most of America or the New World.", answer: "Spain"},
    Turkey = {question: "This country used to be the Ottoman Empire.", answer: "Turkey"},
    United_Kingdom = {question: "This country's empire was the biggest in all of human history.", answer: "United Kingdom"},
    United_States = {question: "This country is the land of the free and home of the brave.", answer: "United States"},
];

len = questions.length;
    
for (var i = 0; i < len; i++) {
        var num = Math.floor(Math.random() * questions.length);
        response = prompt(questions[num].question);
        if (response == questions[num].answer) {
            questions.splice(num, 1);
            alert("Correct!")
        } else {
            incorrectQuestions.push(questions[num]);
            alert("Incorrect.")
            questions.splice(num, 1);
            
        }
}   
    
console.log(incorrectQuestions)

var calculateScore = function() {
    return ((len-incorrectQuestions.length)/len)*100
}

score = calculateScore()

document.write("Your score was : " + String(score) + "% <br>")
document.write(String((len-incorrectQuestions.length)) + "/" + String(len) + "<br><br>")
document.write("Incorrect Questions : <br>")
for (var i = 0; i < incorrectQuestions.length; i++) {
    document.write("Question : " +  incorrectQuestions[i].question + "<br> Answer : " + incorrectQuestions[i].answer + "<br><br>")
}