class Good:

    def __init__(self, name, brand, price, rating, quantity, marketplace_id):
        self.name = name
        self.price = price
        self.brand = brand
        self.rating = rating
        self.quantity = quantity
        self.marketplace_id = marketplace_id

    def save(self, db):
        result = db.execute_query(
            'INSERT INTO good (name, brand, price, rating, quantity, marketplace_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id',
            (self.name, self.brand, self.price, self.rating, self.quantity, self.marketplace_id)
        )
        self.id = result[0]

    @classmethod
    def get_all(self, db):
        try:
            result = db.execute_query('SELECT * FROM good', ())
            if result:
                print('Database of goods:')
                for good in result:
                    print(f'id: {good[0]} | fk_id: {good[1]} | name: "{good[2]}" | price: {good[3]} | '
                          f'brand: {good[4]} | rating: {good[5]} | quantity: {good[6]}')
            else:
                print('No current data')
        except:
            print('Something went wrong')

    def __str__(self):
        return f'"{self.name}" ID: {self.id}'


