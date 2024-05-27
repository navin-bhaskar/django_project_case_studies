from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __repr__(self) -> str:
        return f'"{self.title}" By {self.author}'
