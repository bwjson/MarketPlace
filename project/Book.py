class Book:
    id_count = 0

    def __init__(self, name, author, published_year, rating, number_of_pages):
        Book.id_count += 1
        self.id = Book.id_count
        self.name = name
        self.author = author
        self.published_year = published_year
        self.rating = rating
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f'"{self.name}" written by {self.author} in {self.published_year}, ID: {self.id}'

book1 = Book('Three Comrades', 'Remarque', 1936, 8, 421)
book2 = Book('Four Comrades', 'Remarque', 1936, 8, 421)
print(book1, book2, sep='\n')