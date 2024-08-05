class Good:

    def __init__(self, name, brand, price, rating, quantity, marketplace_id):
        self.name = name
        self.price = price
        self.brand = brand
        self.rating = rating
        self.quantity = quantity
        self.marketplace_id = marketplace_id

    def save(self, db):
        try:
            result = db.execute_query(
                'INSERT INTO good (name, brand, price, rating, quantity, marketplace_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id',
                (self.name, self.brand, self.price, self.rating, self.quantity, self.marketplace_id)
            )
            self.id = result[0]
        except:
            print('Something went wrong')

    @classmethod
    def update(cls, db, id, marketplace_id, name=None, brand=None, price=None, rating=None, quantity=None):
        try:
            result = db.execute_query(
                'SELECT name, brand, price, rating, quantity FROM good WHERE id = (%s) AND marketplace_id = (%s)',
                (id, marketplace_id)
            )

            if not result:
                print(f'No good found with id: {id} and marketplace_id: {marketplace_id}')
                return

            current_values = result[0]

            name = name if name is not None else current_values[0]
            brand = brand if brand is not None else current_values[1]
            price = price if price is not None else current_values[2]
            rating = rating if rating is not None else current_values[3]
            quantity = quantity if quantity is not None else current_values[4]

            db.execute_query(
                'UPDATE good SET name = (%s), brand = (%s), price = (%s), rating = (%s), quantity = (%s) WHERE id = (%s) AND marketplace_id = (%s)',
                (name, brand, price, rating, quantity, id, marketplace_id)
            )
        except Exception as e:
            print(f'Something went wrong: {e}')
    @classmethod
    def remove(cls, db, id):
        try:
            db.execute_query(
                'DELETE FROM good WHERE id = (%s)',
                (id,)
            )
        except:
            print('Something went wrong')


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


