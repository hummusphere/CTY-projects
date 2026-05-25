#create function
def str_to_int(string):
    #check if the number is a float point or integer
    if str(float(string)) == string:
        #transform float to integer
        integer = float(string)
        integer = round(integer)
        integer = int(integer)
        #return integer
        return integer
    else:
        #return integer
        integer = int(string)
        return integer
    
#ask user for input
first_number = input('Enter your first number : ')
first_number = str_to_int(first_number)

#ask user for second input
second_number = input('Enter your second number : ')
second_number = str_to_int(second_number)

#ask user for third input
count_by = input('Enter the number you want to count by: ')
count_by = str_to_int(count_by)

#create range function
total = 0
for num in range(first_number, second_number+1, count_by):
    total = total + int(num)
    print(num)

#print total
print('Total is : %s' total)
