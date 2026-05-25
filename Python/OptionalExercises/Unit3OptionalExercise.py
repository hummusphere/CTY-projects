# Enter information and assign varible names

#price of car
value_of_car = 35000  # <- Enter price of car

#monthly interest rate
monthly_intrest_rate = 0.05 # <- Enter interest rate (in decimals)

#total number of months
months = 60 # <- Enter total months of loan

#----------------------------------------------------------------------------------

#divide the interest rate by 12 (becuase there are 12 months in a year)

#yearly interest rate
yearly_interest_rate = monthly_intrest_rate/12

#calculate round and print the final result
total_price = (yearly_interest_rate * value_of_car)/(1-(1+ yearly_interest_rate)**-months)

#round the number
total_price = round(total_price)

#print the final result
print(total_price)


