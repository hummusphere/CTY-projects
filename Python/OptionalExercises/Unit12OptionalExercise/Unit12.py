#Print List
def print_list():
    shopping_list = open('ShoppingList.txt')
    list_read = shopping_list.read()
    print(list_read)

#Add items
def add_item(item):
    shopping_list = open('ShoppingList.txt', 'a')
    list_write = shopping_list.write('\n' + item)

#subtract items
def subtract(list2):
    num = ''
    for count in range(0,len(list2)):
        num = num + list2[count]
    shopping_list3 = open('ShoppingList.txt', 'w')
    list_read3 = shopping_list3.write(num)

    print('Succsefully deleted item')

#subtract item function
def subtract_item(item):
    shopping_list2 = open('ShoppingList.txt')
    list_read2 = shopping_list2.readlines()
    list2 = []
    for count in range(0, len(list_read2)):
        list2.append(list_read2[count])
        if item+'\n' == list_read2[count]:
            list2.remove(item+'\n')
        elif item == list_read2[count]:
            list2.remove(item)
    subtract(list2)

#loop        
true = bool(1+1== 2)
while true:
#print options
    print('''
1. Show list
2. Add item to list
3. Remove item from list
4. Exit program
''')
    #ask for input
    answer = input('Select Option : ')

    #function options
    #Prints list
    if answer == '1':
        print_list()
    #add items
    if answer == '2':
        answerTwo = input('Item name : ')
        add_item(answerTwo)

    #subtract items
    if answer == '3':
        answerThree = input('Item name : ')
        subtract_item(answerThree)
    #Exit program
    if answer == '4':
        print('\nExiting Program')
        break
