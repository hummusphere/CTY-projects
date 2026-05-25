#import random module
import random

#Print Rules
print('''Reminders : 
- Only enter integers and decimals.
- Only enter \'yes\' or \'no\' for questions.
- Everytime you answer a question you get one point.
- Question consist of random numbers with a random operation.''')

#Assign Points
points = 0

#this loop will repeat forever becuase 1 + 1 will always be equal to 2. 
while 1+1 == 2:

    #get the two random integers 
    number_one = random.randint(1,20)
    number_two = random.randint(1,20)

    #choose random mathmatical operation
    symbol = random.choice(['+', '-', 'x', '/'])

    #if program chooses the '+' operation
    if symbol == '+':

        #tell the player the equation
        equation = 'Question : %s + %s = ? : ' % (str(number_one), str(number_two))

        #figure out the answer
        answer = number_one + number_two

        #Ask the player
        user_answer = input(equation)

        #check if answer is correct
        if float(user_answer) == float(answer):

            #add point, print congratualons, and ask if they want to continue.
            points = points + 1
            print('Correct! +1 point! Current Points : %s!' % points)
            answer = input('Would you like to contiune? Enter \'yes\' or \'no\' : ')

            #if answer = no then thank player and break loop.
            if answer == 'no':
                print('Total Score : %s. Thank you for playing' % points)
                break;
            elif answer == 'yes':
                continue;
            else:
                print('Error : answer was not in a \'yes\', \'no\' form.')
                break;

        #if the answer is wrong then ask the player to continue.
        else:
            answer = input('Incorrect, do you wish to continue? Enter yes or no : ')
            if answer == 'no':
                break;
            elif answer == 'yes':
                continue;
            else:
                print('Error : answer was not in a \'yes\', \'no\' form.')
                break;

    #if program chooses the '-' operation
    if symbol == '-':

        #tell the player the equation
        equation = 'Question : %s - %s = ? : ' % (str(number_one), str(number_two))

        #figure out the answer
        answer = number_one - number_two

        #Ask the player
        user_answer = input(equation)

        #check if answer is correct
        if float(user_answer) == float(answer):

            #add point, print congratualons, and ask if they want to continue.
            points = points + 1
            print('Correct! +1 point! Current Points : %s!' % points)
            answer = input('Would you like to contiune? Enter \'yes\' or \'no\' : ')

            #if answer = no then thank player and break loop.
            if answer == 'no':
                print('Total Score : %s. Thank you for playing' % points)
                break;
            elif answer == 'yes':
                continue;
            else:
                print('Error : answer was not in a \'yes\', \'no\' form.')
                break;
            
        #if the answer is wrong then ask the player to continue.
        else:
            answer = input('Incorrect, do you wish to continue? Enter yes or no : ')
            if answer == 'no':
                break;
            elif answer == 'yes':
                continue;
            else:
                print('Error : answer was not in a \'yes\', \'no\' form.')
                break;

    #if program chooses the 'x' operation
    if symbol == 'x':

        #tell the player the equation
        equation = 'Question : %s x %s = ? : ' % (str(number_one), str(number_two))

        #figure out the answer
        answer = number_one * number_two

         #Ask the player
        user_answer = input(equation)

        #check if answer is correct
        if float(user_answer) == float(answer):

            #add point, print congratualons, and ask if they want to continue.
            points = points + 1
            print('Correct! +1 point! Current Points : %s!' % points)
            answer = input('Would you like to contiune? Enter \'yes\' or \'no\' : ')

            #if answer = no then thank player and break loop.
            if answer == 'no':
                print('Total Score : %s. Thank you for playing' % points)
                break;
            elif answer == 'yes':
                continue;
            else:
                print('Error : answer was not in a \'yes\', \'no\' form.')
                break;

        #if the answer is wrong then ask the player to continue.
        else:
            answer = input('Incorrect, do you wish to continue? Enter yes or no : ')
            if answer == 'no':
                break;
            elif answer == 'yes':
                continue;
            else:
                print('Error : answer was not in a \'yes\', \'no\' form.')
                break;
            
    #if program chooses the '/' operation
    if symbol == '/':

        #tell the player the equation
        equation = 'Question : %s / %s = ? : ' % (str(number_one), str(number_two))

        #figure out the answer
        if number_one > number_two:
            answer = number_one / number_two
        else:
            answer = number_two / number_one

        #Ask the player
        user_answer = input(equation)

         #check if answer is correct
        if float(user_answer) == float(answer):

            #if the answer is wrong then ask the player to continue.
            points = points + 1
            print('Correct! +1 point! Current Points : %s!' % points)
            answer = input('Would you like to contiune? Enter \'yes\' or \'no\' : ')

            #if answer = no then thank player and break loop.
            if answer == 'no':
                print('Total Score : %s. Thank you for playing' % points)
                break;
            elif answer == 'yes':
                continue;
            else:
                print('Error : answer was not in a \'yes\', \'no\' form.')
                break;

        #if the answer is wrong then ask the player to continue.
        else:
            answer = input('Incorrect, do you wish to continue? Enter yes or no : ')
            if answer == 'no':
                break;
            elif answer == 'yes':
                continue;
            else:
                print('Error : answer was not in a \'yes\', \'no\' form.')
                break;
