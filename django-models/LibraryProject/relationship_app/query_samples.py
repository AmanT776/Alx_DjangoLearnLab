from . import models

def query_all_books_by_author(author_name):
    author = models.Author.objects.get(name=author_name)
    books = models.Book.objects.filter(author=author)
    for book in books:
        print(f"{book.id} {book.title}")

def list_all_books_in_library(library_name):
    library = models.Library.objects.get(name=library_name)
    books = library.books.all()  
    for book in books:
        print(book.title)


def retrieve_librarian_for_library(library_name):
    library = models.Library.objects.get(name=library_name)
    librarian = library.librarian  
    print(librarian.name)
