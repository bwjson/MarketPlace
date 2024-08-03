class Good:

    def __init__(self, name, brand, price, rating, quantity):
        self.name = name
        self.price = price
        self.brand = brand
        self.rating = rating
        self.quantity = quantity

    def __str__(self):
        return f'"{self.name}" ID: {self.id}'


