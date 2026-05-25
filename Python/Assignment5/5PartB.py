#-----------------------------------------------------------------------------------------------------------------------------

#Ask user for information
total_distance = input('Enter total distance here : ')
total_hour_per_day_driving = input('Enter total hour per day driving here : ')
average_miles_per_hour = input('Enter average miles per hour here : ')
average_miles_per_gallon = input('Enter average miles per gallon here : ')
average_gas_price_per_gallon = input('Enter average gas price per gallon here : ')
motel_cost_per_night = input('Enter average motel cost per night : ')

#-----------------------------------------------------------------------------------------------------------------------------

#calulate gas price
def calculate_gas_price(total_distance, average_miles_per_gallon, average_gas_price_per_gallon):
    gallons = float(total_distance) / float(average_miles_per_gallon)
    gas_price = float(gallons) * float(average_gas_price_per_gallon)
    return (gas_price)

#Print gas price
gas_price = calculate_gas_price(total_distance, average_miles_per_gallon, average_gas_price_per_gallon)
print('The cost of gas is %s.' % gas_price)

#------------------------------------------------------------------------------------------------------------------------------

#calculate motel cost
def calculate_motel_price(total_distance, total_hour_per_day_driving, average_miles_per_hour, motel_cost_per_night):
    miles_per_day = float(total_hour_per_day_driving) * float(average_miles_per_hour)
    nights = float(total_distance) / float(miles_per_day)
    motel_cost = float(nights) * float(motel_cost_per_night)
    return motel_cost

#print motel cost
motel_cost = calculate_motel_price(total_distance, total_hour_per_day_driving, average_miles_per_hour, motel_cost_per_night)
print('The motel cost is %s.' % motel_cost)

#-------------------------------------------------------------------------------------------------------------------------------

#print total cost
total_cost = float(gas_price) + float(motel_cost)
total_cost = str(total_cost)
print('The total cost is : ' + total_cost)

#-------------------------------------------------------------------------------------------------------------------------------


    
