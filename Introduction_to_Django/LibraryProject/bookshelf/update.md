>>> from bookshelf.models import Book
>>> book = Book.objects.get(id=1)
>>> book.title = "limitless"
>>> book.publication_year = 2014
>>> book.save()
>>> book
# <Book: Book object (1)>