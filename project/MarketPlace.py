from Book import Book


class MarketPlace:
    id_count = 0

    def __init__(self, name, city, country):
        MarketPlace.id_count += 1
        self.id = MarketPlace.id_count
        self.name = name
        self.city = city
        self.country = country
        self.goods = []

    def add_good(self, good):
        if isinstance(good, Book):
            self.goods.append(good)
            print(f'Good ID: {good.id} was successfully added'
                  f'to {self.name} Shop ID: {self.id}')
        else:
            raise ValueError("Your good's type was considered as a book")

    def remove_good(self, good):
        if isinstance(good, Book):
            self.goods.remove(good)
            print(f'Good ID: {good.id} was successfully removed'
                  f'from {self.name} Shop ID: {self.id}')
        else:
            raise ValueError("Your good's type was considered as a book")

    def display_goods(self):
        if self.goods and len(self.goods) > 0:
            for good in self.goods:
                print(f'Good ID: {good.id} Name: {good.name} Rating: {good.rating}')
        else:
            print('The shop is empty. There is no goods')

    def find_good(self, good_id):
        for good in self.goods:
            if good.id == good_id:
                print(f'Your good is {good.name} with ID: {good.id}')
                return
        return None



