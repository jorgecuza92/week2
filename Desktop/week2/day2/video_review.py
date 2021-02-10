
# Store Model
# stores = []

# class Store:
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address
#         self.items = []
#     def add_item(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity


# print("1. Add store: ")
# print("2. add item to store: ")
# print('3. View all: ')
# print('q. Quit: ')


# while True:
#     choice = input("Enter choice: ")
#     if choice == "1":
#         store_name = input("Enter store name: ")
#         store_address = input("Enter store address: ")
#         store = Store(store_name, store_address)
#         stores.append(store)
#     elif choice == 2:
#         for index in range(0, len(stores)):
#             store = stores[index]
#             print(f"{index + 1} {store.name} - {store.address}")
#         store_index = int(input('Choose store to add items: '))
#         store = stores[stores_index - 1]
#         item_name = input('enter item name: ')
#         item_price = float(input('enter price: '))
#         item = Item(item_name, item_price)
#         # add item to store
#         store.items.append(item)

    
#     elif choice == "3":
#         for store in stores:
#             print(f"{store.name} - {store.address}")
#             for item in store.items:
#                 print(f"{item.name} - ${item.price}")


#     elif choice == 'q':
#         break

# INHERITANCE 

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model 


    def drive(self):
        print('DRIVE')

    def fill_up(self):
        print('FILL UP')

car = Car("Audi", "TT")
car.drive()
car.fill_up()

class ElectricCar(Car):
    def __init__(self, make, model):
        super().__init__(make, model)
electric_car = ElectricCar('Audi', 'TT')
electric_car.drive()
electric_car.fill_up()

class ElectricScooter(ElectricCar): # inherits ElectricCar and Car
    def __init__(self, make, model):
        super().__init__(make, model)
