from django.db import migrations

def insert_data(apps, schema_editor):
    #Countries (places of residence)
    Residence = apps.get_model("molodkina_books", "Residence")
    Country_CS = Residence(Name = 'Czechoslovakia')
    Country_CS.save()
    Country_FR = Residence(Name = 'France')
    Country_FR.save()
    Country_RU = Residence(Name = 'Russia')
    Country_RU.save()
    Country_GR = Residence(Name = 'Greece')
    Country_GR.save()
    Country_ENG = Residence(Name = 'England')
    Country_ENG.save()
    Country_DE = Residence(Name = 'Germany')
    Country_DE.save()
    Country_US = Residence(Name = 'United States')
    Country_US.save()
    Country_CH = Residence(Name = 'Switzerland')
    Country_CH.save()
    Country_PR = Residence(Name = 'Prussia')
    Country_PR.save()
    Country_AFG = Residence(Name = 'Afghanistan')
    Country_AFG.save()
    Country_IRN = Residence(Name = 'Iran')
    Country_IRN.save()
    Country_IRE = Residence(Name = 'Ireland')
    Country_IRE.save()
    
    #Authors
    Author = apps.get_model("molodkina_books", "Author")

    voltaire = Author(Name = 'Voltaire',
    YearOfBirth = 1694,
    YearOfDeath = 1778,
    PlaceOfBirth = 'France',
    PlaceOfDeath = 'France')
    voltaire.save()

    nabokov = Author(Name = 'Vladimir Nabokov',
    YearOfBirth = 1899,
    YearOfDeath = 1977,
    PlaceOfBirth = 'Russia',
    PlaceOfDeath = 'Switzerland')
    nabokov.save()

    beckett = Author(Name = 'Samuel Beckett',
    YearOfBirth = 1906,
    YearOfDeath = 1989,
    PlaceOfBirth = 'Ireland',
    PlaceOfDeath = 'France')
    beckett.save()

    kundera = Author(Name = 'Milan Kundera',
    YearOfBirth = 1929,
    PlaceOfBirth = 'Czechoslovakia')
    kundera.save()

    hosseini = Author(Name = 'Khaled Hosseini',
    YearOfBirth = 1965,
    PlaceOfBirth = 'Afghanistan')
    hosseini.save()

    #Assigning nationalities to authors
    voltaire.Residence.add(Country_FR, Country_ENG, Country_PR, Country_CH)
    nabokov.Residence.add(Country_RU, Country_GR, Country_ENG, Country_DE, Country_CS, Country_FR, Country_US, Country_CH)
    beckett.Residence.add(Country_IRE, Country_FR)
    kundera.Residence.add(Country_CS, Country_FR)
    hosseini.Residence.add(Country_AFG, Country_IRN, Country_FR, Country_US)
        
    #Books
    Book = apps.get_model("molodkina_books", "Book")

    #Books by Voltaire
    Book(Title = 'Upon the Civil Wars of France, Extracted from Curious Manuscripts and Upon Epic Poetry of the European Nations, from Homer Down to Milton',
    Language = 'English',
    YearOfPublication = 1727,
    Author = voltaire).save()

    Book(Title = 'Letters on the English',
    Language = 'French',
    YearOfPublication = 1733,
    Author = voltaire).save()

    Book(Title = 'Candide',
    Language = 'French',
    YearOfPublication = 1759,
    Author = voltaire).save()

    #Books by Nabokov
    Book(Title = 'The Gift',
    Language = 'Russian',
    YearOfPublication = 1938,
    Author = nabokov).save()

    Book(Title = 'Lolita',
    Language = 'English',
    YearOfPublication = 1955,
    Author = nabokov).save()

    Book(Title = 'Pnin',
    Language = 'English',
    YearOfPublication = 1957,
    Author = nabokov).save()

    Book(Title = 'Pale Fire',
    Language = 'English',
    YearOfPublication = 1962,
    Author = nabokov).save()

    #Books by Beckett

    Book(Title = 'Murphy',
    Language = 'English',
    YearOfPublication = 1938,
    Author = beckett).save() 

    Book(Title = 'Watt',
    Language = 'English',
    YearOfPublication = 1953,
    Author = beckett).save()  

    Book(Title = 'Endgame',
    Language = 'French',
    YearOfPublication = 1957,
    Author = beckett).save()

    Book(Title = 'Molloy',
    Language = 'French',
    YearOfPublication = 1951,
    Author = beckett).save()

    Book(Title = 'Malone Dies',
    Language = 'French',
    YearOfPublication = 1951,
    Author = beckett).save()

    Book(Title = 'The Unnamable',
    Language = 'French',
    YearOfPublication = 1953,
    Author = beckett).save()

 
    #Books by Kundera
    Book(Title = 'The Joke',
    Language = 'Czech',
    YearOfPublication = 1967,
    Author = kundera).save()

    Book(Title = 'The Unbearable Lightness of Being',
    Language = 'Czech',
    YearOfPublication = 1985,
    Author = kundera).save()

    Book(Title = 'Identity',
    Language = 'French',
    YearOfPublication = 1995,
    Author = kundera).save()

    Book(Title = 'Ignorance',
    Language = 'French',
    YearOfPublication = 2000,
    Author = kundera).save()

    #books by hosseini
    Book(Title = 'The Kite Runner',
    Language = 'English',
    YearOfPublication = 2003,
    Author = kundera).save()

    Book(Title = 'A Thousand Splendid Suns',
    Language = 'English',
    YearOfPublication = 2007,
    Author = kundera).save()

    
class Migration(migrations.Migration):

    dependencies = [
        ('molodkina_books', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(insert_data)
    ]