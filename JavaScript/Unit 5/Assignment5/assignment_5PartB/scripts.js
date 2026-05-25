// Sets up rows

var rows = [
    row1 = ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    row2 = ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    row3 = ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    row4 = ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    row5 = ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    row6 = ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    row7 = ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    row8 = ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    row9 = ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    row10 = ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"]
];



randomColumn = (Math.ceil(Math.random() * 10)) - 1
randomRow = (Math.ceil(Math.random() * 10)) -1 

computerColumn = (Math.ceil(Math.random() * 10)) - 1
computerRow = (Math.ceil(Math.random() * 10)) - 1

alert("In this game you will have to choose a column and row. The computer will also choose a column and row. Whoever is closer wins!")

playerColumn = parseInt(prompt("Choose your column : ")) - 1
playerRow = parseInt(prompt("Choose your row : ")) - 1

document.write("Your point : X" + "<br>")
document.write("Computer point : M" + "<br>")
document.write("Actual point : H" + "<br><br>")


replace = rows[randomRow]
replace[randomColumn] = "H"

replace = rows[computerRow]
replace[computerColumn] = "M"

replace = rows[playerRow]
replace[playerColumn] = "X"

for (var i = 0; i < rows.length; i++) {
    for (var e = 0; e < rows[i].length; e++){
        row = rows[i]
        document.write(row[e])
    }
    document.write("<br>")
}

computerDistance = Math.sqrt(((randomRow - computerRow)**2)+((randomColumn - computerColumn)**2))
playerDistance = Math.sqrt(((randomRow - playerRow)**2)+((randomColumn - playerColumn)**2))


console.log(computerDistance )

if (playerDistance < computerDistance) {
    document.write("<br>" + "You won!" + "<br>")
} else {
    document.write("<br>" + "You lost." + "<br>")
}

document.write("Your distance : " + String(playerDistance) + "<br>")
document.write("Computer distance : " + String(computerDistance))
