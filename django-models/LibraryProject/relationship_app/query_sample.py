from . import models

def books_by_author(author_name):
    author = models.Author.objects.get(name=author_name)
    books = models.Book.objects.filter(author=author)
    for book in books:
        print(f"{book.id} {book.title}")

def books_in_library(library_name):
    library = models.Library.objects.get(name=library_name)
    books = models.Book.objects.filter(library=library)
    for book in books:
        print(book.title)

def librarian_in_library(library_name):
    library = models.Library.objects.get(name=library_name)
    librarians = models.Librarian.objects.filter(library=library)
    for librarian in librarians:
        print(librarian.name)
