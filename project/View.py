from MarketPlace import MarketPlace
from Book import Book

def main():
    marketplace = MarketPlace('Ozon', 'Astana', 'Kazakhstan')
    good = Book('Three Comrades', 'Remarque', 1936, 8, 421)

    print('Hello, here is your command menu\n'
          '1 - Add good\n'
          '2 - Remove good\n'
          '3 - Display all goods\n'
          '4 - Find book by ID\n'
          '5 - Exit')

    while True:
        choice = int(input())
        if choice == 1:
            marketplace.add_good(good)
            continue
        elif choice == 2:
            marketplace.remove_good(good)
            continue
        elif choice == 3:
            marketplace.display_goods()
            continue
        elif choice == 4:
            marketplace.find_good(good.id)
            continue
        elif choice == 5:
            break
        else:
            print('Please choose another command')



if __name__ == '__main__':
    main()

# connect with database, choosing which marketplace and which good i want to access, add additional methods for creating objects itself