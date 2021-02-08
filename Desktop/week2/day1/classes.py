
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.color = ''
        self.speed = 0
        self.current_gear = 'N'
    #private function available only inside the class
    def change_color():
        pass

    def change_gear(self, gear):
        self.current_gear = gear

    def drive(self):    # must pass self
        self.speed = 40
        # calling change_gear function from within a function
        self.change_gear('4')

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed = 0


# creating an object of the Car class
car = Car('Honda', 'Accord')
print(car.speed) # will be 0
# calling drive function on that car object/instance
car.drive()     # car.property name... car.function name
print(car.speed) # 40 because car.drive() function was called
car.brake()
print(car.speed)    # speed is 0 brake() was called

car.change_gear('1')
car.change_gear('N')
car.change_gear('3')

car.accelerate()
print(car.speed)
car.accelerate()
print(car.speed)


class Tree:
    def __init__(self):
        self.species = ''
        self.width = ""
        self.height = ""
        self.age = ""

tree = Tree()
tree.species = 'OAK'
tree.width = "10"
tree.age = "30"