#Ask for information

nights = int(input('Number of nights staying : '))
guests = int(input('Number of people staying : '))

if guests == 1:
    cost = 50 * nights
    #print cost
    print('The cost is %s.' % cost)

if guests == 2:
    cost = 75 * nights
    #print cost
    print('The cost is %s.' % cost)

if guests == 3:
    cost = 200 * nights
    #print cost
    print('The cost is %s.' % cost)

if guests == 4:
    cost = 300 * nights
    #print cost
    print('The cost is %s.' % cost)

