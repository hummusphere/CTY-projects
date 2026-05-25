#imports random module
import random

#creates die class
class die:
        #defines instance
        def __init__(self, text):
                self.text = text

        #creates roll function
        def roll():
            #chooses fandom number
            faceValue = random.randint(1,6)
            #chooses face
            if faceValue == 1:
                face = '-----------\n|          |\n|          |\n|    o    |\n|          |\n|          |\n-----------'
            elif faceValue == 2:
                face = '-----------\n|          |\n|          |\n|    o    |\n|    o    |\n|          |\n-----------'
            elif faceValue == 3:
                 face = '-----------\n|         |\n|    o    |\n|    o    |\n|    o    |\n|          |\n-----------'
            elif faceValue == 4:
                face = '-----------\n|          |\n|          |\n|   o o  |\n|   o o  |\n|          |\n-----------'
            elif faceValue == 5:
                face = '-----------\n|          |\n|   o o  |\n|    o    |\n|   o o  |\n|          |\n-----------'
            elif faceValue == 6:
                face = '-----------\n|          |\n|   o o  |\n|   o o  |\n|   o o  |\n|          |\n-----------'
            return face + '\n' + str(faceValue)

        #return face and faceValue
        def __str__(self):
                return self.text

#create DieGame Class
class DieGame():
    #Define instances
    def __init__(self,Dice1, Dice2):
        self.Dice1 = Dice1
        self.Dice2 = Dice2
    #Prints dice and number
    def play(self):
        print(die(self.Dice1))
        print(die(self.Dice2))
        
        
#Creates forever loop
while 1+1 ==2:
        #creates objects
        DieObj1 = die.roll()
        DieObj2 = die.roll()

        #uses diegame function
        game = DieGame(DieObj1, DieObj2)
        game.play()

        #asks user if they want to play again
        answer = input('Would you like to play again? (yes/no) : ')
        if answer == 'no':
                break

        






