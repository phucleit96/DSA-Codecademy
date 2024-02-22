class Menu:
    # Constructor method for Menu class
    def __init__(self, name, items, start_time, end_time):
        # Initialize attributes of the menu
        self.name = name  # Name of the menu
        self.items = items  # Dictionary containing items and their prices
        self.start_time = start_time  # Start time when the menu is available
        self.end_time = end_time  # End time when the menu is available

    # Method to return a string representation of the menu
    def __repr__(self):
        return f"{self.name} will be available from {self.start_time} to {self.end_time}."

    # Method to calculate the total bill for purchased items
    def calculate_bill(self, purchased_items):
        bill = 0
        for item in purchased_items:
            bill += self.items[item]  # Add the price of each purchased item to the bill
        return bill


class Franchise:
    # Constructor method for Franchise class
    def __init__(self, address, menus):
        # Initialize attributes of the franchise
        self.address = address  # Address of the franchise location
        self.menus = menus  # List of menus available at the franchise location

    # Method to return a string representation of the franchise
    def __repr__(self):
        return f"The address of the restaurant is {self.address}"

    # Method to find available menus at a given time
    def available_menus(self, time):
        suitable_menus = []
        for menu in self.menus:
            # Check if the given time falls within the availability of each menu
            if menu.start_time <= time <= menu.end_time:
                suitable_menus.append(menu)  # Add the menu to the list of suitable menus
        return suitable_menus


class Business:
    # Constructor method for Business class
    def __init__(self, name, franchises):
        # Initialize attributes of the business
        self.name = name  # Name of the business
        self.franchises = franchises  # List of franchise locations belonging to the business


# Dictionary of items and their prices for the brunch menu
items_brunch = {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50,
    'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

# Create an instance of the Menu class representing the brunch menu
brunch = Menu("Brunch", items_brunch, 11, 16)

# Dictionary of items and their prices for the early bird menu
items_early = {
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00,
    'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50,
    'coffee': 1.50, 'espresso': 3.00
}

# Create an instance of the Menu class representing the early bird menu
early_bird = Menu("Early-bird Dinners", items_early, 15, 18)

# Dictionary of items and their prices for the dinner menu
items_dinner = {
    'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00,
    'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50,
    'coffee': 2.00, 'espresso': 3.00
}

# Create an instance of the Menu class representing the dinner menu
dinner = Menu("Dinner", items_dinner, 17, 23)

# Dictionary of items and their prices for the kids' menu
items_kid = {
    'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

# Create an instance of the Menu class representing the kids' menu
kids = Menu("Kid Menu", items_kid, 11, 21)

# List containing all the menus available at the restaurant
all_menus = [brunch, early_bird, dinner, kids]

# Create an instance of the Franchise class representing the flagship store
flagship_store = Franchise("1232 West End Road", all_menus)

# Create an instance of the Franchise class representing the new franchise location
new_installment = Franchise("12 East Mulberry Street", all_menus)

# List containing all the franchise locations of the business
all_stores = [flagship_store, new_installment]

# Create an instance of the Business class representing the first business
first_business = Business("Basta Fazoolin' with my Heart", all_stores)

# Dictionary of items and their prices for the arepas menu
items_menu = {
    'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

# Create an instance of the Menu class representing the arepas menu
arepas_menu = Menu("Menu", items_menu, 10, 20)

# Create an instance of the Franchise class representing the arepas place
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

# Create an instance of the Business class representing the second business
second_business = Business("Take a' Arepa", [arepas_place])

# Test cases
print(brunch.calculate_bill(["pancakes", "coffee", "home fries"]))  # Calculate bill for brunch items
print(early_bird.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"]))  # Calculate bill for early bird items

print(flagship_store.available_menus(12))  # Print available menus at flagship store at 12 PM
print(flagship_store.available_menus(17))  # Print available menus at flagship store at 5 PM

print(arepas_place.available_menus(20))  # Print available menus at arepas place at 8 PM
