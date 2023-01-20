from django.db import migrations

def insert_data(apps, schema_editor):
    Country = apps.get_model("molodkina_books", "Country")
    Country1 = Country(Name = 'Czechia')
    Country1.save()
    Country2 = Country(Name = 'France')
    Country2.save()

    Author = apps.get_model("molodkina_books", "Author")

    kundera = Author(Name = 'Milan Kundera',
    YearOfBirth = 1929,
    PlaceOfBirth = 'Czechia')

    kundera.save()
    kundera.Nationalities.add(Country1,Country2)

    Book = apps.get_model("molodkina_books", "Book")

    Book(Title = 'The Joke',
    Language = 'Czech',
    YearOfPublication = 1967,
    Author = kundera).save()

    Book(Title = 'Slowness',
    Language = 'French',
    YearOfPublication = 1995,
    Author = kundera).save()

class Migration(migrations.Migration):

    dependencies = [
        ('molodkina_books', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(insert_data)
    ]
