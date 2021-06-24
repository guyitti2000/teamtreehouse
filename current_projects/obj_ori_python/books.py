class Book:
   def __init__(self, author, title):
       self.author = author
       self.title = title

   def __str__(self):
       return f'{self.author} {self.title}'

class Bookcase:
   def __init__(self):
       self.books = []

   def __iter__(self):
       yield from self.books

   def add_book(self, book):
       self.books.append(book)

book = Book('John Green', 'Paper Towns')
print(book)
