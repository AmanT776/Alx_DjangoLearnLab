from bookshelf.models import Book

# retrieve the book first
book = Book.objects.get(title="1984")

# update its title
book.title = "Nineteen Eighty-Four"
book.save()

print(book)
