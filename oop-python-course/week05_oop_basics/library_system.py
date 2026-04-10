class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_book(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Year:", self.year)
        print()

# Create objects
book1_shnn = Book("Python Programming", "John Smith", 2022)
book2_shnn = Book("Data Structures", "Jane Doe", 2021)
book3_shnn = Book("OOP Concepts", "Mark Lee", 2020)

# Display books
book1_shnn.display_book()
book2_shnn.display_book()
book3_shnn.display_book()