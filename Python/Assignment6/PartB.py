#Ask user for information

ballons = int(input('How many ballons will you be buying? : '))

#Calculate Cost

if ballons <= 50:
    #Print Cost
    print('The cost is %s.' % ballons)

if ballons > 50 and ballons <=100:
    cost = ballons * 0.5
    #Print Cost
    print('The cost is %s.' % cost)

if ballons > 100:
    cost = ballons * .25
    #Print Cost
    print('The cost is %s.' % cost)
