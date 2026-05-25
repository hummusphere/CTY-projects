#Make the roof
print('|' * 32)
#loop that repeats 3 times
for make_floor in range(0,3):
    #make the top of the window
    print('|' + ' ' * 5 + '*' * 10 + ' ' * 6  + '*' * 10 + ' ' * 6 + '|')
    #loop that makes the body of the window
    for make_window in range(0, 6):
        print('|' + ' ' * 5 + '*' + ' ' * 14 +  '*' +  ' ' * 6 + '*' + ' ' * 14 +  '*'+  ' ' * 6+'|')
    #prints bottom of the window
    print('|' + ' ' * 5 + '*' * 10 + ' ' * 6  + '*' * 10 + ' ' * 6 + '|')
    print('|' + '-' * 29 + ' |')

#Makes bottom of the building
print('|' * 32)
