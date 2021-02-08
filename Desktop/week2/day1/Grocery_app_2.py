stores = []

class Store:
  def __init__(self, name, address):
    self.name = name
    self.address = address
    self.items = []

class Grocery_item:
  def __init__(self, name, price, quantity):
    self.name = name
    self.price = price
    self.quantity = quantity

def show_stores():
    index = 1
    for store in stores:
        print(f"{index}: {store.name} - {store.address}")

def show_items():
    index = 0
    for store in stores:
        print(f"{index + 1}: {store.name} - {store.address}")
        for item in stores[index].items:
            print(f"item: {item.name} \nprice: ${item.price} \nquantity: {item.quantity}")

def display():
    print("Enter 1 to add a store: ")
    print("Enter 2 to add item to a store: ")
    print("Enter 3 to view store and items: ")
    print("Enter q to quit: ")

while True:
  display()
  choice = input("Enter choice: ")
  if choice == "1":
    store_name = input("Enter store name: ")
    store_address = input("Enter store address: ")
    store = Store(store_name, store_address)
    stores.append(store)
  elif choice == "2":
    # display all stores
    show_stores()
    store_selector = int(input('choose store number: '))
    name = input('name of item: ')
    price = input('price of item: ')
    quantity = input('quantity of item: ')
    new_item = Grocery_item(name, price, quantity)
    stores[store_selector - 1].items.append(new_item)
  elif choice == "3":
    show_items()
  elif choice == 'q':
      break
  else:
      print('invalid entry, execution failed.')