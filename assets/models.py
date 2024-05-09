from django.db import models
import datetime

from school_library.models import Author


class Book(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='asset_books')

    def __str__(self):
        return self.title


class Magazine(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Newspaper(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Asset(models.Model):
    asset_book = models.ForeignKey(Book, null=True, blank=True, on_delete=models.CASCADE)
    asset_magazine = models.ForeignKey(Magazine, null=True, blank=True, on_delete=models.CASCADE)
    asset_newspaper = models.ForeignKey(Newspaper, null=True, blank=True, on_delete=models.CASCADE)

    transaction_date = models.DateField(default=datetime.date.today)
    quantity = models.IntegerField()
    amount = models.FloatField() 

    @property
    def asset(self):
        if self.asset_book_id is not None:
            return self.asset_book
        if self.asset_magazine_id is not None:
            return self.asset_magazine
        if self.asset_newspaper_id is not None:
            return self.asset_newspaper
        raise AssertionError("Asset is not set")

    def __str__(self):
        return f'{self.quantity} {repr(self.asset)} for {self.amount}'