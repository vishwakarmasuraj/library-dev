from django.db import models
from django.urls import reverse


class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    published_date = models.DateField()
    pages = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('libraryapp:book_edit', kwargs={'pk': self.pk})