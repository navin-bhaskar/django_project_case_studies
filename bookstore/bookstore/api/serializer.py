from rest_framework import serializers

from api.models import Book


class BookItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("id", "title", "author", "genre", "published_date", "price")
