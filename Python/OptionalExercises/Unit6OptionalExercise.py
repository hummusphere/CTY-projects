gallons_used = int (input ('How much water has the costumer used this quarter?') )

if gallons_used <= 25000:

    gallons_used = (gallons_used *2.35)/1000
    print('The costumer\'s bill is %s' % gallons_used)
    
elif gallons_used > 25000 and gallons_used <= 50000:

    bill = gallons_used - 25000
    gallons_used = ( 25000 * 2.35) / 1000 +  (bill * 6.6)/1000
    print('The costumer\'s bill is %s' % gallons_used)
    
else:

     bill = gallons_used - 50000
     gallons_used = (25000 * 2.35)/1000 + (25000 * 6.60) / 1000 + (bill * 8.84)/1000
     print('The costumer\'s bill is %s' % gallons_used)

        
     
