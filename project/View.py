from DB import Database
def main():
    db = Database('marketplace', 'postgres', '5432', 'localhost')
    Database.connect(db)
    db.close()


if __name__ == '__main__':
    main()

# CRUD for marketplace and goods