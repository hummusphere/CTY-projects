#Enter Users Grades Below

python_grade = '96'
java_grade = '91'
math_grade = '98'

#----------------------------------------------------------------------------

#Assign Varibles
space = ' '
dash = '-'
equal = '='

#---------------------------------------------------------------------------


#Print Text
print((space * (31)) + ('Report Card'))
print((space*20) + ('Course Name') + (space* (10)) + ('Course Grade'))

#Print Dashes
print(75* dash)

#Print Course Name And Course Grade
print(space)
print((space*22) + 'Python' + (space * 19) + (python_grade))
print((space*22) + 'Java' + (space * 21) + (java_grade))
print((space*22) + 'Math' + (space * 21) + (math_grade))

#Print Equals
print(75* equal)

#Calculat total amount of points
python = int(python_grade)
java = int(java_grade)
math = int(math_grade)
total = python + java + math
total = str(total)

#Print total
print((space*22)+ 'Total' + (space*19) + total)

#Calculate Average
total = int(total)
total = (total/300) * 100
total = str(total)

#Print Average 
print((space*22)+ 'Average' + (space * 17) + total)


      
