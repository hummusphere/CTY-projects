#create a list
thelist = []
#make a while loop that runs forever
while 'true' == 'true':
    #ask for a number
    number = input('Enter Number : ')
    #make sure it is a integer
    if str.isdigit(number) == bool('true' == 'true'):
        #add number to list
        thelist.append(int(number))
        #ask user to continue
        answer = input('Succsefully added number to list, would you like to continue? (yes/no) : ')
        #break loop
        if answer == 'no':
            break
    else:
        #Ask user for a valid integer
        print('Please enter a valid integer.')

#print information
print('Your list is : %s' % thelist)
print('The length of your list is %s.' % len(thelist))
print('The maximum value of your list is %s.' % max(thelist))
print('The minimum value of your list is %s.' % min(thelist))
if len(thelist) > 1:
    print('The range of your list is %s.' % (max(thelist) - min(thelist)))
else:
    print('The range of your list is 0.')
#calculate average
total = 0
for num in range(0, len(thelist)):
    total = total + int(thelist[num])
print('The average of your list is %s.' % str(int(total)/int(len(thelist))))
    
