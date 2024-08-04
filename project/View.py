from DB import Database
from MarketPlace import MarketPlace
from Good import Good
def main():
    db = Database('marketplace', 'postgres', '5432', 'localhost')
    db.connect()

    # marketplace = MarketPlace('Ozon', 'Astana', 'Kazakhstan')
    # marketplace.save(db)

    # marketplace_id = MarketPlace.get_id(db, 'Ozon')

    # good = Good('Three Comrades', 'Litres', 200.00, 8.00, 213, marketplace_id)
    # good.save(db)

    # MarketPlace.get_all(db)
    # Good.get_all(db)

    db.close()


if __name__ == '__main__':
    main()

# CRUD for marketplace and goods