from rest_framework import serializers
from .models import Author, Category, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author_details = AuthorSerializer(source='author', read_only=True)
    category_details = CategorySerializer(source='category', read_only=True)

    class Meta:
        model = Book
        fields = [
            'id', 'title', 'author', 'author_details',
            'category', 'category_details', 'isbn',
            'description', 'published_date', 'available_copies',
            'created_at', 'updated_at'
        ]

    def validate_available_copies(self, value):
        if value < 0:
            raise serializers.ValidationError("عدد النسخ المتوفرة لا يمكن أن يكون سالباً.")
        return value