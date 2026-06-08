class Customer:

    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address

    # this method needs other method to change the address, so this relationship is called aggregation.
    def edit_profile(self, new_name, new_city, new_state):
        self.name = new_name
        self.address.change_address(new_city, new_state)


class Address:

    def __init__(self, city, state):
        self.city = city
        self.state = state


    def change_address(self, new_city, new_state):
        self.city = new_city
        self.state = new_state


hussains_address = Address("Fasisalabad", "Punjab")
hussain = Customer("Hussain", "Male", hussains_address)
hussain.edit_profile("Hussain Ali", "Lahore", "Punjab")

print(hussain.name) # Hussain Ali
print(hussain.address.city) # Lahore
print(hussain.address.state) # Punjab