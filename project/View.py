from DB import Database
from MarketPlace import MarketPlace
from Good import Good

def main():
    db = Database('marketplace', 'postgres', '5432', 'localhost')
    db.connect()

    # create
    # marketplace = MarketPlace('Ozon', 'Astana', 'Russia')
    # marketplace.save(db)
    # marketplace_id = MarketPlace.get_id(db, 'Ozon')
    # good = Good('Summer Time', 'Litres', 200.00, 8.00, 213, marketplace_id)
    # good.save(db)

    # read
    # MarketPlace.get_all(db)
    # Good.get_all(db)

    # update
    # MarketPlace.update(db, 2, name='Ozon', city='Moscow')
    # Good.update(db, 2, 2, name='Berserk', price=400.00)

    # delete
    # Good.remove(db, 7)
    # MarketPlace.remove(db, 3)

    db.close()


if __name__ == '__main__':
    main()

# switch console controller