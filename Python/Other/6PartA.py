#Ask for information

nights = int(input('Number of nights staying : '))
guests = int(input('Number of people staying : '))

if guests > 2:
   suite = input('Would you like a Deluxe Suite (Type \'d\') or a Penthouse (type \'p\') : ')
   if suite == 'd':
       suite = int(200)
   elif suite == 'p' :
       suite = int(300)
    

if guests == 1:
    cost = 50 * nights
    #print cost
    print('The cost is %s.' % cost)

if guests == 2:
    cost = 75 * nights
    #print cost
    print('The cost is %s.' % cost)

if guests >= 3:
    cost = suite * nights
    #print cost
    print('The cost is %s.' % cost)



