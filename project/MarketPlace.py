class MarketPlace:

    def __init__(self, name, city, country):
        self.name = name
        self.city = city
        self.country = country
        self.id = None

    def save(self, db):
        try:
            result = db.execute_query(
                'INSERT INTO marketplace (name, city, country) VALUES (%s, %s, %s) RETURNING id',
                (self.name, self.city, self.country)
            )
            self.id = result[0]
        except:
            print('Something went wrong')

    @classmethod
    def update(cls, db, id, name=None, city=None, country=None):
        try:
            result = db.execute_query(
                'SELECT name, city, country FROM marketplace WHERE id = (%s)',
                (id,)
            )

            if not result:
                print(f'No marketplace found with id: {id}')
                return

            current_values = result[0]

            name = name if name is not None else current_values[0]
            city = city if city is not None else current_values[1]
            country = country if country is not None else current_values[2]

            db.execute_query(
                'UPDATE marketplace SET name = (%s), city = (%s), country = (%s) WHERE id = (%s)',
                (name, city, country, id)
            )
        except Exception as e:
            print(f'Something went wrong: {e}')

    @classmethod
    def remove(cls, db, id):
        try:
            db.execute_query(
                'DELETE FROM good WHERE marketplace_id = (%s)',
                (id,)
            )
            db.execute_query(
                'DELETE FROM marketplace WHERE id = (%s)',
                (id,)
            )
        except:
            print('Something went wrong')

    @classmethod
    def get_all(cls, db):
        try:
            result = db.execute_query('SELECT * FROM marketplace', ())
            if result:
                print('Database of marketplaces:')
                for marketplace in result:
                    print(f'id: {marketplace[0]} | name: "{marketplace[1]}" | city: {marketplace[2]} | country: {marketplace[3]}')
            else:
                print('No current data')
        except:
            print('Something went wrong')

    @classmethod
    def get_id(cls, db, name):
        result = db.execute_query(f'SELECT id FROM marketplace WHERE name=%s', (name,))
        if result:
            return result[0][0]
        else:
            return None

    def __str__(self):
        return f'"{self.name}" ID: {self.id}'





