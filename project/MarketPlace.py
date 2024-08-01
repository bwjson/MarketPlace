from Book import Book, book1, book2


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

    def display_goods(self):
        if self.goods and len(self.goods) > 0:
            for good in self.goods:
                print(f'Good ID: {good.id} Name: {good.name} Rating: {good.rating}')
        else:
            print('The shop is empty. There is no goods')


ozon1 = MarketPlace('Ozon', 'Astana', 'Kazakhstan')

MarketPlace.add_good(ozon1, book1)
MarketPlace.add_good(ozon1, book2)
MarketPlace.display_goods(ozon1)