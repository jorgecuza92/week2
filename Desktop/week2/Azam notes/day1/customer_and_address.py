
class Customer:
    def __init__(self, name):
        self.name = name
        self.addresses = [] # array to represent multiple addresses
        # self.street = ''
        # self.state =  ''
        # self.city = ''
        # self.zip_code = ''

class Address:
    def __init__(self, street, city, state, zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code


customer = Customer('John Doe')
print(customer.addresses)
address = Address('525 Yale st', 'Houston', 'TX', '77007')
another_address = Address('345 poo st', 'houston', 'tx', '77505')
# How toa dd address to a customer
customer.addresses.append(address)
customer.addresses.append(another_address)
print(customer.addresses)

# Display customer and addresses
print()
print(customer.name)
for address in customer.addresses:
    print(address.street)
    print(address.state)

# customer.street = '525 Yale St'
# customer.city = 'Houston'
# customer.state = 'TX'
# customer.zip_code = '77007'