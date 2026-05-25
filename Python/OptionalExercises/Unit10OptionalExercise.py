#Create class called vehicle
class Vehicle:

    #Define instances
    def __init__ (self, name, make, price):
        self.name = name
        self.make = make
        self.price = price

    #create ride function
    def ride (self):
        print('Riding %s' % self.name)

    #create str function
    def __str__ (self):
        return 'Vehicle name : ' + self.name + '. Vehicle make : ' + self.make + '. Vehicle Price : ' + self.price

#crate subclass
class PoweredVehicle(Vehicle):

    #overide instances
    def __init__ (self, name, make, regestration, price):
        Vehicle.__init__(self, name, make, price)
        self.regestration = regestration

    #create refuel function
    def refuel (self):
        print('Refueling')

#Create subclass
class Bicycle(Vehicle):

    #overide instances
    def __init__ (self, name, make, biketype, price):
        Vehicle.__init__(self, name, make, price)
        self.biketype = biketype         

    #create function
    def pedal (self):
        print('Pedaling')

    #create function
    def ride (self):
        print('Peadling my %s' % self.name)

    #return str function
    def __str__ (self):
        return 'Bike name : ' + self.name + '. Bike make : ' + self.make + '. Bike Price : ' + self.price + '. Bike Type : ' + self.biketype

#create subclass
class Car (PoweredVehicle):

    #create ride function
    def ride (self):
        print('Driving my %s on the road.' % self.name)

#create subclass
class Ship (PoweredVehicle):

    #create ride function
    def ride (self):
        print('Sailing the %s over the sea.' % self.name)

#print classes and use the ride() function
car = Car('Highlander', 'Toyota', '1234', '$35000')
print(car)
car.ride()
car.refuel()
bicycle = Bicycle('Orbea Orca Areo', 'Areo', 'Race Bike', '$6000')
print(bicycle)
bicycle.ride()
ship = Ship('Two Maersk', 'Shipping Line', '4321', '21,000,000,000')
print(ship)
ship.ride()
ship.refuel()

