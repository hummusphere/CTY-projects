#Since 1+1 is allways equal to 2 this program will run forever
while 1+1==2:

    def encyrpt(text):

        #Reset Codeword
        codeword = ''

        #Loop that repats legnht of the text
        for num in range(0, len(text)):

            #translates the word
            translate = encyrption[text[num]]

            #adds the translated word to the sentence
            codeword = codeword + translate

        #Prints final codeword
        print('The encyrption is : %s' % codeword)
        decyrpt(codeword)

    #shows the translated version of each letter

    def decyrpt(text):
        #Reset Codeword
        codeword = ''

        #Loop that repats legnht of the text
        for num in range(0, len(text)):

            #translates the word
            translate = decyrption[text[num]]

            #adds the translated word to the sentence
            codeword = codeword + translate

        #Prints final codeword
        print('The decyrption is : %s' % codeword) 

    #shows the translated version of each letter

    encyrption = {
                  'a' : 'd',
                  'b' : 'e',
                  'c' : 'f',
                  'd' : 'g',
                  'e' : 'h',
                  'f' : 'i',
                  'g' : 'j',
                  'h' : 'k',
                  'i' : 'l',
                  'j' : 'm',
                  'k' : 'n',
                  'l' : 'o',
                  'm' : 'p',
                  'n' : 'q',
                  'o' : 'r',
                  'p' : 's',
                  'q' : 't',
                  'r' : 'u',
                  's' : 'v',
                  't' : 'w',
                  'u' : 'x',
                  'v' : 'y',
                  'w' : 'z',
                  'x' : 'a',
                  'y' : 'b',
                  'z' : 'c',
                  ' '  : ' ',}

    decyrption = {
                  'd' : 'a',
                  'e' : 'b',
                  'f' : 'c',
                  'g' : 'd',
                  'h' : 'e',
                  'i' : 'f',
                  'j' : 'g',
                  'k' : 'h',
                  'l' : 'i',
                  'm' : 'j',
                  'n' : 'k',
                  'o' : 'l',
                  'p' : 'm',
                  'q' : 'n',
                  'r' : 'o',
                  's' : 'p',
                  't' : 'q',
                  'u' : 'r',
                  'v' : 's',
                  'w' : 't',
                  'x' : 'u',
                  'y' : 'v',
                  'z' : 'w',
                  'a' : 'x',
                  'b' : 'y',
                  'c' : 'z',
                  ' '  : ' ',}

    #asks user to add text to encyrpt
    Text = input('Encrypt Message : ')
    encyrpt(Text)

    
    
