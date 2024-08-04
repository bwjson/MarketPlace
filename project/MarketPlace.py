class MarketPlace:

    def __init__(self, name, city, country):
        self.name = name
        self.city = city
        self.country = country
        self.id = None

    def save(self, db):
        result = db.execute_query(
            'INSERT INTO marketplace (name, city, country) VALUES (%s, %s, %s) RETURNING id',
            (self.name, self.city, self.country)
        )
        self.id = result[0]

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





