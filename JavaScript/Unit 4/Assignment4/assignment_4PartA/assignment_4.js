var length = parseInt(prompt("How long should the histogram be?"));

for (var firstNum = 0; firstNum < length; firstNum ++) 
{
    for (var secondNum = 0; secondNum != firstNum; secondNum ++) 
    {
        document.write("@")
    }
    
    if (secondNum != 0) {
        document.write(firstNum)
        document.write("<br>")
    }
}
for (var firstNum = length; firstNum > 0; firstNum --) 
{
    for (var secondNum = 0; secondNum != firstNum; secondNum ++) 
    {
        document.write("@")
    }
    
    document.write(firstNum)
    document.write("<br>")
}