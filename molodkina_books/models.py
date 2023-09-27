from django.db import models

# Create your models here...
class Residence(models.Model):
    Name = models.CharField(max_length=250)
    def __str__(self):
        return self.Name

class Author(models.Model):
    Name = models.CharField(max_length=250)
    YearOfBirth = models.IntegerField()
    YearOfDeath = models.IntegerField(blank=True, null=True)
    PlaceOfBirth = models.CharField(max_length=250)
    PlaceOfDeath = models.CharField(max_length=250, blank=True, null=True)
    Residence = models.ManyToManyField(Residence)
    def __str__(self):
        return self.Name

class Book(models.Model):
    Author = models.ForeignKey('Author', on_delete=models.CASCADE)
    Title = models.CharField(max_length=250)
    Language = models.CharField(max_length=250)
    YearOfPublication = models.IntegerField()
    def __str__(self):
        return self.Title

