class Item:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.name} (price: {self.price}, description: {self.description}, size: {self.dimensions})"

class User:
    def __init__(self, name, surname, phone):
        self.name = name
        self.surname = surname
        self.phone = phone

    def __str__(self):
        return f"{self.name} {self.surname}, phone: {self.phone}"

class Purchase:
    def __init__(self, user):
        self.user = user
        self.items = {}  #number

    def add_item(self, item, quantity):
        self.items[item] = quantity

    def __str__(self):
        text = f"User: {self.user}\nItems:"
        for item, quantity in self.items.items():
            text += f"\n- {item.name}: {quantity} pcs."
        text += f"\nTotal: {self.get_total()} UAH"
        return text

    def get_total(self):
        return sum(item.price * quantity for item, quantity in self.items.items())

lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )
print(lemon)  # lemon, price: 5

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""
print (isinstance(cart.user, User) is True, 'Екземпляр класу User')
print (cart.get_total() == 60, "Всього 60")
print(cart.get_total() == 60, 'Повинно залишатися 60!')
cart.add_item(apple, 10)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 10 pcs.
"""

print (cart.get_total() == 40)