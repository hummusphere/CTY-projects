themes = [orange = ["rgb(255, 174, 0)", "rgb(255, 190, 48)"], red = ["rgb(255 0 0)", "rgb(255 48 48)"], blue=["rgb(0 132 255)","rgb(48 150 255)"], green = ["rgb(0 255 0)","rgb(48 255 83)"]]


var startLoop = function() {
    setTimeout(function(){
        for (var i = 0; i < 1; i++) {
            var color = themes[Math.floor((Math.random()*4))]
            $("#header").css("background-color", color[0])
            $("#nav").css("background-color", color[1])
        }
    startLoop()}, 2000);
}



currentCountries = [
    Brazil = {name: "Brazil", link: "images/Brazil.png"},
    Canada = {name: "Canada", link: "images/Canada.png"},
    China = {name: "China", link: "images/China.png"},
    Egypt = {name: "Egypt", link: "images/Egypt.png"},
    Germany = {name: "Germany", link: "images/Germany.png"},
    India = {name: "India", link: "images/India.png"},
    Italy = {name: "Italy", link: "images/Italy.png"},
    Japan = {name: "Japan", link: "images/Japan.png"},
    Mexico = {name: "Mexico", link: "images/Mexico.png"},
    Russia = {name: "Russia", link: "images/Russia.png"},
    Spain = {name: "Spain", link: "images/Spain.png"},
    Turkey = {name: "Turkey", link: "images/Turkey.png"},
    United_Kingdom = {name: "United Kingdom", link: "images/United_Kingdom.png"},
    United_States = {name: "United States", link: "images/United_States.png"}
]

incorrectCountries = []


$(document).ready(function() {
    lastScore = localStorage.getItem("lastScore")
    if (lastScore != null) {
        $("#h4").html("Welcome Back! Your last score : " + lastScore)
    }
});


var startQuiz = function() {
    $("#h4").html("What country is this flag from?")
    $("#quiz").hide()
    userCorrect = false
    random = Math.floor((Math.random()*currentCountries.length))
    $("#mainImg").css("display", "block")
    $("#submit").css("display", "block")
    $("#input").css("display", "block")
    $("#mainImg").attr("src", currentCountries[random].link)
    document.getElementById("submit").onclick = function(){
        if ($("#input").val() == currentCountries[random].name) {
            currentCountries.splice(random,1)
            $("#input").val("")
            if (currentCountries.length == 0) {
                $("#mainImg").css("display", "none")
                $("#submit").css("display", "none")
                $("#input").css("display", "none")
                score = (100 - Math.floor((incorrectCountries.length/14)*100))
                localStorage.setItem("lastScore", score)
                $("#h4").html("Good Job! Your score was : " + score + "%")
            } else {
                startQuiz()
            }
         } else {
            $("#h4").html("Try Again!")
            incorrectCountries.push(currentCountries[random])
        }  
    };
     
}

