#Car:
# - model
# - make
# - vin
# - color

# creating Car class and defining properties of the class.
class Car:
    def __init__(self, make = "Honda", model = "accord"):       # assigned default values for parameters for make and model. If nothing is passed make and model will be Honda, Accord
        self.make = make
        self.model = model
        self.vin = ''
        self.color = ''
        self.no_of_cylinders = 2

# create an instance/object of the Car class
car = Car("Toyota", "Sienna")   # passing in arguments for make, model
print(car.make) # Honda
car.make = 'Toyota'
car.model = 'Sienna'
car.color = 'white'
car.vin = 'ASKFLJASDLFJLSDK' # you can also change make and model like this as well
car.no_of_cylinders = 4

new_car = Car('Tesla', 'Model S')
new_car.color = 'black'
new_car.vin = 'ASLDKFjLK'


# car.make
# car.model
# car.vin
# car.color

# another_car = Car()
# print(another_car.make) ???

# THEY ARE NOT EQUAL, B/C OBJECTS ARE CREATED AND COMPARED BY REFERENCE.
# if car == another_car:

# BankAccount
# - account number
# - routing number
# - account owner
# - account type (checkings, savings)
# - balance
# - name
#
# required properties to create an account:
# - account owner (firstname, lastname, middle)
# - account type (checkings, savings)
# - balance (default value of 0)

# Create a class called Table to reprent a table
# in order to create an instance of the table, you must pass width height of table
print()
print()


class Table:
    def __init__(self, width, height): # self is initializer/constructor
        self.width = width
        self.height = height
        self.color = ''
        self.materials = ''
        self.style = ''

table = Table(36, 48)
table.style = 'modern contemporary'
table.color = 'cafe brown'
table.materials = 'zebra wood'
print(table.width)
print(table.height)


