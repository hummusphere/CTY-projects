#Enter Information Below
state = ['Maryland', 'Pennsylvania', 'Virginia']
population = ['6.052', '12.81', '7']
area = ['12407', '46055', '40000']

#-----------------------------------------------------------------------

#Assign Varibles
space = ' '
dash = '-'

#-----------------------------------------------------------------------------

#Print the outputs
print('State' + space * 10 + 'Population (in millions)' + space * 7 + 'Area(in square miles)')
print(dash * 70)

#Print state, poulation, and area
print(state[0] + space * 16 + population[0] + space * 25 + area[0])
print(state[1] + space * 12 + population[1] + space * 25 + area[1])
print(state[2] + space * 18 + population[2] + space * 27 + area[2])
