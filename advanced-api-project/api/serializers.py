from rest_framework import serializers
from .models import Book, Author

# Serializer for the Book model
# This will handle conversion of Book model instances to JSON (and vice versa).
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        # '__all__' means include all fields from the Book model:
        # id, title, publication_year, author
        fields = '__all__'
    def validate(self, data):
        if len(data['title']) < 5:
            raise serializers.ValidationError("Title must be at least 5 characters long.")
        return data



# Serializer for the Author model
# This includes a nested representation of the author's related books.
class AuthorSerializer(serializers.ModelSerializer):
    # Define a nested serializer for the books.
    # "books" comes from the related_name in the Book model's ForeignKey field.
    # many=True → because one author can have multiple books.
    # read_only=True → prevents creating/updating books directly inside the author serializer.
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        # Only include the author's name and the nested list of books in the API response.
        fields = ['name', 'books']
