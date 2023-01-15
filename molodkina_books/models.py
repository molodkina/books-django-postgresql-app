from django.db import models

# Create your models here.
class Book(models.Model):
    BookID = models.AutoField(primary_key=True)
    BookTitle = models.CharField(max_length=250)
    Language = models.CharField(max_length=250)
    Year = models.IntegerField()
    def __str__(self):
        return self.BookTitle

class Book_Author(models.Model):
    BookID = models.ForeignKey(Book, on_delete=models.CASCADE)
    AuthorID = models.AutoField(primary_key=True)
    def __str__(self):
        return f'BookID is {self.BookID} and AuthorID is {self.AuthorID}'

class Author(models.Model):
    AuthorID = models.AutoField(primary_key=True)
    AuthorName = models.CharField(max_length=250)
    def __str__(self):
        return self.AuthorID