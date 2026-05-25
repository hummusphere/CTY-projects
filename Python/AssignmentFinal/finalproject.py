#create book class
class book:
    #init function
    def __init__ (self, book, author, genre, price):
        self.book = book
        self.author = author
        self.genre = genre
        self.price = price
    #str function
    def __str__ (self):
        return 'Book Name : ' +  str(self.book)+' \nAuthor Name : '+str(self.author)+'\nGenre : '+str(self.genre)+'\nPrice : $'+str(self.price) 

#create inventory class
class inventory():
    #add book method
    def add_book():
        #code that enters in data from list into map
        booklist = open('booklist.txt')
        lines = booklist.readlines()
        for count in range(0, len(lines)):
            placeHolder = lines[count].split(',')
            Map[str(placeHolder[0])] = str(book(str(placeHolder[1]), str(placeHolder[2]),str(placeHolder[3]), str(placeHolder[4])))

    #display list method
    def display_list ():
        #code that prints out information from inventory
        secondHolder = 999
        for count in range(0, 5):
            secondHolder = int(secondHolder) + 1
            secondHolder = str(secondHolder)
            print('=' * 40)
            print('Item Number : %s' % secondHolder)
            print(Map[secondHolder])

#creates cart subclass
class Cart (inventory):
    #adds book to list
    def add_book(bookId):
        bookList.append('Book ID : ' + bookId+ '\n'+Map[bookId])
        print('Book added to cart')
    #prints all the books in your cart
    def show_books():
        if len(bookList) == 0:
            print('\nYour cart is empty\n')
        else:
            for count in range(0, len(bookList)):
                print('=' * 40)
                print(bookList[count])
    #code that splits book information until it gets
    #the price, then adds all of the prices together to get the total
    def checkout():
        if len(bookList) == 0:
            print('\nNothing In cart\n')
        else:
            total = 0
            for count in range (0,len(bookList)):
                varibleHolder = bookList[count]
                varibleHolder2 = varibleHolder.split('\n')
                num = ''
                for count in range(0, len(varibleHolder2)):
                    num = num + varibleHolder2[count]
                num2 = num.split(' : $')
                length = len(num2)
                total = total + float(num2[length-1])
            print('\nYour total is $%s.\n' % str(total))
            loopTrue = false

#bools
loopTrue = bool(1)
false = bool(0)
#lists/maps
Map = {}
bookList = []
#adds books to list
inventory.add_book()

#loop
while loopTrue:
    #shops options
    print('1: Display Books\n2: Add To Cart\n3: Show Cart\n4: Checkout\n5: Quit\n')
    #asks for input
    optionSelected = input('Select Option : ')
    #maks sure input is valid
    if optionSelected != '1' and optionSelected != '2' and optionSelected != '3' and optionSelected != '4' and optionSelected != '5':
        print('That is not a valid option.\n')
    #Option 1
    elif optionSelected == '1':
        inventory.display_list()
    #Option 2
    elif optionSelected == '2':
        answer = input('\nEnter Book Id : ')
        if answer != '1000' and answer != '1001' and answer != '1002' and answer != '1003' and answer != '1004':
            print('\nThat is not a valid Id\n')
        else:
            Cart.add_book(answer)
    #Option 3
    elif optionSelected == '3':
        Cart.show_books()
    #Option 4
    elif optionSelected == '4':
        Cart.checkout()
    #Option 5
    elif optionSelected == '5':
        print('Thank you for shopping.')
        break


