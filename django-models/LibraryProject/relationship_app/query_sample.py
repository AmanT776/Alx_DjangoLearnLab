from . import models

def get_book_by_author(author_name):
    author = models.Author.objects.get(name=author_name)
    books = models.Book.objects.filter(author_id=author.id)
    for book in books:
        print(f"{book.id} {book.name}")

def get_all_books():
    books = models.Book.objects.all()
    for book in books:
        print(book.name)

def get_librarian(library_name):
    library = models.Library.objects.get(name=library_name)
    librarians = models.Librarian.objects.filter(Library_id=library.id)
    for librarian in librarians:
        print(librarian.name)
        
        



