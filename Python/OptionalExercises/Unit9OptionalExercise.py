#import random module
import random

#make three lists
fulllist = []
oddnums = []
evennums = []

#loop
for num in range(0,100):

    #pick random number
    number = random.randint(0,100)

    #add number to the full list
    fulllist.append(number)

    #check if number is even or odd
    if number % 2 == 0:

        #add number to the even list
        evennums.append(number)
    else:
        #add number to the odd list
        oddnums.append(number)
    
#Print the full list
print('Full list :')
print(fulllist)

#space
print(' ')

#print odd numbers
print('Odd list : ')
print(oddnums)

#space
print(' ')

#print even numbers
print('Even list : ')
print(evennums)
