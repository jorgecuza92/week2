# Car:
#    - model
#    - make
#    - vin
#    - color

# creating a Car class and definining the properties of the class.
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.vin = ""
        self.color = ""
        self.no_of_cylinders = 2

    # create an instance/object of the Car class


car = Car("Toyota", "Corolla")
car.color = "white"
car.vin = "ASDADAS2343"
car.no_of_cylinders = 4

new_car = Car("Tesla", "Model X")
new_car.color = "black"
new_car.vin = "ASDASFA3333"

print(car.make)
print(car.model)

# print(car.make) # Honda
# car.make = "Toyota"
# car.model = "Sienna"

# another_car = Car()
# print(another_car.make)

# they are NOT equal. Because objects are created and compared by reference
# if car == another_car:


BankAccount
- account
number
- routing
number
- account
owner
- account
type(checking, savings)
- balance
- name

required
properties
to
create
an
account:
- account
owner(firstname, lastname, middlename)
- account
type(checking, savings)
- balance(default
value
of
0)

# Create a class called Table to represent a table
# In order to create an instance of the table, you must pass in width and height of the table