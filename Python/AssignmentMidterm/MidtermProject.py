#Since 1+1 is allways equal to 2 this program will run forever
while 1+1==2:

    def encyrpt(text):

        #Reset Codeword
        codeword = ''

        #Loop that repats legnht of the text
        for num in range(0, len(text)):

            translate = ord(text[num])
            
            if translate > 119:
                letter = chr((translate + 3) - 26)

            elif translate == 32:
                letter = ' '
                
            else:
                letter = chr(translate + 3)
                
            #adds the translated word to the sentence
            codeword = codeword + letter

        #Prints final codeword
        print('The encyrption is : %s' % codeword)
        decyrpt(codeword)

    def decyrpt(text):
        #Reset Codeword
        codeword = ''

        #Loop that repats legnht of the text
        for num in range(0, len(text)):

            translate = ord(text[num])

            if translate < 100 and not translate == 32:
                letter = chr((translate -3) + 26)

            elif translate == 32:
                letter = ' '
                
            else:
                letter = chr(translate + -3)

            #adds the translated word to the sentence
            codeword = codeword + letter

        print('The dycyrption is : %s' % codeword)

    #asks user to add text to encyrpt
    Text = input('Encrypt Message : ')
    encyrpt(Text)

    
    
