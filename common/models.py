from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)  # author name

    def __str__(self):
        return self.name

    @property
    def books(self):
        return str(', '.join(self.books_set.values_list('title', flat=True)) if self.books_set.exists() else '--//--')


class Book(models.Model):
    title = models.CharField(max_length=100)
    pages_count = models.PositiveIntegerField()  # count pages for a book
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='books_set')

    def __str__(self):
        return self.title

