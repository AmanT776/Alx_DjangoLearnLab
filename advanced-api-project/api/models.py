from django.db import models

# The Author model represents a book author in the database.
# Each Author has only a "name" field here
class Author(models.Model):
    # Name of the author (max 30 characters).
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

# The Book model represents a book written by an Author.
# Each Book has a title, a publication year, and is linked to an Author.
class Book(models.Model):
    # Title of the book (max 30 characters).
    title = models.CharField(max_length=30)

    # The year the book was published (stored as an integer).
    publication_year = models.IntegerField()

    # Relationship: Many books can belong to one author.
    # 'related_name="books"' lets us access all books of an author with author.books.all()
    # 'on_delete=models.CASCADE' means if an Author is deleted, all their books will be deleted as well.
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return self.title