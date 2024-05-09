from django.db import models


class Author(models.Model):
    firstname = models.CharField(max_length=256)
    middlename = models.CharField(max_length=256, blank=True, null=True)
    lastname = models.CharField(max_length=256)
    date_of_birth = models.DateField()
    date_of_death = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    citizenship = models.CharField(max_length=256)
    language = models.CharField(max_length=256)

    def __str__(self):
        return self.lastname


class Book(models.Model):
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books')
    title = models.CharField(max_length=1024)

    def __str__(self):
        return self.title