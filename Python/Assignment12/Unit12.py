#import module that checks file sizes
import os

#Creates two lists
name = []
contact = []

#opens files
contactBook = open('ContactBook')
numberBook = open('NumberBook')

#Reads lines
contactLines = contactBook.readlines()
numberLines = numberBook.readlines()

#sends name file data into a list
for count in range(0, len(contactLines)):
    if '\n' in contactLines[count]:
        name.append(contactLines[count].replace('\n', ''))
    else:
        name.append(contactLines[count])

#sends contact file data into a list
for count in range(0, len(numberLines)):
    if '\n' in numberLines[count]:
        contact.append(numberLines[count].replace('\n', ''))
    else:
        contact.append(numberLines[count])

#Option 1 - Add/Update

def optionOne():
    
#Ask user for input
    print('''
1 - Add
2 - Update''')
    update_or_add = input('Enter to continue :')
    #Makes sure input is valid
    if update_or_add != '1' and update_or_add != '2':
        print('That is not a valid option')
    else:
        #Ask for input
        if update_or_add == '1':
            nameTwo = input('''
Name of Contact :''')

            #adds name to file and list
            contactBook = open('ContactBook', 'a')
            if os.stat('ContactBook').st_size != 0:
                contactBook.write('\n')
            contactBook.write(nameTwo)
            contactBook.close()
            name.append(nameTwo)
            contactTwo = input('''
Number/Email : ''')
            #Adds contact to file and list
            numberBook = open('NumberBook', 'a')
            if os.stat('NumberBook').st_size != 0:
                numberBook.write('\n')
            numberBook.write(contactTwo)
            numberBook.close()
            contact.append(contactTwo)

        #Updates name and contact
        elif update_or_add == '2':

            #asks for user input
            oldname = input('Contact Name: ')
            updatename = input('New Contact Name : ')
            if len(name) == 0:
                print('No Contact Found')
            else:
                #changes contact in lists and files
                updateTrue = ''
                for num in range(0, len(name)):
                    if name[num]== oldname:
                        name.remove(name[num])
                        name.append(updatename)
                        updateTrue = 'true'
                        numTwo = num
                        contactBook = open('ContactBook', 'w')
                        num = ''
                        for count in range(0, len(name)):
                            if count != len(name):
                                num = num + name[count]+'\n'
                            else:
                                num = num + name[count]
                        contactBook.write(num)
                    else:
                        if updateTrue != 'true':
                            updateTrue = 'false'
                if updateTrue == 'false':
                    print('No Contact Found')
                else:
                    numberBook = open('NumberBook', 'w')
                    updatecontact = input('New Contact Number / Email : ')                  
                    contact.remove(contact[numTwo])
                    contact.append(updatecontact)
                    print('Name And Contact Updated')
                    num = ''
                    for count in range(0, len(contact)):
                        if count != len(contact):
                            num = num + contact[count]+'\n'
                        else:
                            num = num + contact[count]
                    numberBook.write(num)

#Option - 2
def optionTwo():
    if len(name) == 0:
        print('''
No contacts added.''')
    else:
        #print all names in list
        for count in range(0, len(name)):
            print('Contact Name : %s | Contact Number : %s' % (name[count], contact[count]))

#Search for name
def optionThree():
    #Ask for input
    nameThree = input('Enter Contact Name : ')
    if len(name) == 0:
        print('No contact found')
    else:
        #Search and print name
        nameFound = ' '
        for num in range(0, len(name)):
            if name[num] == nameThree:
                print('Name : %s | contact info : %s' % (name[num], contact[num]))
                nameFound  = 'true'
            else:
                if nameFound != 'true':
                    nameFound = 'false'
        if nameFound == 'false' :
            print('No contact found')

#Option 4
def optionFour():
    #Ask for input
    contactFour = input('Contact : ')
    if len(name) == 0:
        print('No contact found.')
    else:
        #delete name from list and replace file with list
        contactFound = ' '
        if len(name) != 1:
            placeHolder = len(name)
        else:
            placeHolder = len(name)
        for num in range(0, placeHolder):
            if name[num] == contactFour:
                contactFound = 'true'
                name.remove(contactFour)
                contact.remove(contact[num])
                contactBook = open('ContactBook', 'w')
                numberBook = open('NumberBook', 'w')
                num = ''
                for count in range(0, len(name)):
                    if count != len(name):
                        num = num + name[count]+'\n'
                    else:
                        num = num + name[count]
                contactBook.write(num)
                num = ''
                for count in range(0, len(contact)):
                    if count != len(contact):
                        num = num + contact[count]+'\n'
                    else:
                        num = num + contact[count]
                numberBook.write(num)
                print('Contact Deleted')
                break
        else:
            if contactFound != 'true':
                contactFound = 'false'
        if contactFound == 'false':
            print('No contact found.')

#Loop
while 1+1==2:
    #print options
    print('''
Select an option...
1 - Add/Update contcat...
2 - Display all contacts...
3 - Search...
4 - Delete contact...
5 - Quit
    ''')
    #Get input and check if its valid
    number = (input('Enter to continue : '))
    if number != '1' and  number != '2'  and  number != '3'  and  number != '4'  and  number != '5':
        print('''
That is not a valid option''')
    else:
        #option 1
        if int(number) == 1:
            optionOne()
        #option 2
        elif int(number)  == 2:
            optionTwo()
        #option 3
        elif int(number)  == 3:
            optionThree()
        #option 4
        elif int(number)  == 4:
            optionFour()
        #option 5
        elif int(number)  == 5:
            break
