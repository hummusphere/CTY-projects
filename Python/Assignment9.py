#Contact Book

#Functions

#Option One

def optionOne():
#Shows User Options
    print('''
1 - Add
2 - Update''')
#Gets users input
    update_or_add = input('Enter to continue :')
#Makes sure the option is valid
    if update_or_add != '1' and update_or_add != '2':
        print('That is not a valid option')
    else:
#Checks to see if the user entered 1
        if update_or_add == '1':
#Asks user for name and contact, then adds the input into the lists.
            nameTwo = input('''
Name of Contact :''')
            name.append(nameTwo)
            contactTwo = input('''
Number/Email : ''')
            contact.append(contactTwo)
#Checks to see if the option is 2
        elif update_or_add == '2':
#Asks user for old name
            oldname = input('Contact Name: ')
#Asks user for new name
            updatename = input('New Contact Name : ')
#Makes sure there are names in the list
            if len(name) == 0:
                print('No Contact Found')
            else:
#Loop that checks every name in the list and updates the name that matches the old name,
#if no such name is found then it prints no contact found.
                for num in range(0, len(name)):
                    if name[num]== oldname:
                        name.remove(name[num])
                        name.append(updatename)
                        updateTrue = 'true'
                        numTwo = num
                    else:
                        updateTrue = 'false'
                if updateTrue == 'false':
                    print('No Contact Found')
                else:
                    updatecontact = input('New Contact Number / Email : ')                  
                    contact.remove(contact[numTwo])
                    contact.append(updatecontact)
                    print('Name And Contact Updated')

#Option Two

#OptionTwo
def optionTwo():
#makes sure that there are names in the lists
    if len(name) == 0:
        print('''
No contacts added.''')
    else:
#loop that prints every name and contact in the lists
        for num in range(0, len(name)):
            print('')
            print('''Name : %s, Contact information : %s''' % (name[num], contact[num]))

#Option Three

def optionThree():
#Asks for user for input
    nameThree = input('Enter Contact Name : ')
#Makes sure there are names in the lists
    if len(name) == 0:
        print('No contact found')
    else:
#loop that looks for the name the user entered then prints it and the
#contact info.
        for num in range(0, len(name)):
            if name[num] == nameThree:
                print('Name : %s, contact info : %s' % (name[num], contact[num]))
                nameFound  = 'true'
            else:
                nameFound = 'false'
        if nameFound == 'false' :
            print('No contact found')

#Option Four

def optionFour():
#asks for user input
    contactFour = input('Contact : ')
#makes sure that there are names in the list
    if len(name) == 0:
        print('No contact found.')
    else:
#loop that looks for the name that the user entered and then deletes it
        for num in range(0, len(name)):
            if name[num]== contactFour:
                print('Deleted Contact')
                contactFound = 'true'
                name.remove(contactFour)
                contact.remove(contact[num])
            else:
                contactFound = 'false'
    if contactFound == 'false':
        print('No contact found.')

#These two lines create the lists
name = []
contact = []

#Loop that will run forever
while 1+1==2:

#Shows the user their options
    print('''
Select an option...
1 - Add/Update contcat...
2 - Display all contacts...
3 - Search...
4 - Delete contact...
5 - Quit
    ''')

#Gets input from user
    number = (input('Enter to continue : '))

#Checks to make sure that the user entered in a valid option
    if number != '1' and  number != '2'  and  number != '3'  and  number != '4'  and  number != '5':

#Tells user that the option they selected is not valid
        print('''
That is not a valid option''')
    else:

#Option 1 - Add / Update
        if int(number) == 1:
            optionOne()

#Option 2 - Display Names
        elif int(number)  == 2:
            optionTwo()
            
#Option 3 - Search Names
        elif int(number)  == 3:
            optionThree()

#Option 4 - Delete Contact
        elif int(number)  == 4:
            optionFour()

#Option 5 - Quit
        elif int(number)  == 5:
            break
