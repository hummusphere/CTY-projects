#import random module
import random

#assign the sum of the even and odd numbers to zero
even_number_sum = 0
odd_number_sum = 0

#loop that repeats 10 times
for nums in range(0, 10):

    #choose random number
    num = random.randint(1,25)

    #test out if even or odd
    even_or_odd = num % 2

    #check if the numbr is even or odd
    if even_or_odd == 0:

         #print the number and say that its even
         print(str(num) +' is even.')
    
        #add the number to the even sum
         even_number_sum = even_number_sum + num
    else:

        #print that the number is odd
        print(str(num) + ' is odd.')

        #add the number to the odd sum
        odd_number_sum = odd_number_sum + num

#print the even and odd sums
print('Even number total is %s' % even_number_sum)
print('Odd number total is %s' % odd_number_sum)

