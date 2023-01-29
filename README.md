#  Exophonic Writers and Their Books
## About the App Service and API

This is a Python web app using the Django framework and the Azure Database for PostgreSQL relational database service. It provides access to my favourite [exophonic](https://en.wiktionary.org/wiki/exophonic) writers and some of the books they've written in their native or second language.

## Available endpoints

### GET /authors
**Request URL:** https://molodkina-books.azurewebsites.net/authors/<br>
**Description:** Returns an array of all writers available in the database.<br>
**Returns Values:**
* Author_id
* Name
* YearOfBirth
* YearOfDeath
* PlaceOfBirth
* PlaceOfDeath

### GET /books
**Request URL:** https://molodkina-books.azurewebsites.net/books<br>
**Description:** Returns an array of all books available in the database.<br>
**Returns Values:**
* Book_id
* Title
* YearOfPublication
* Language
* Author_id<br>

**Parameters**
* YearOfPublication (exact, greater than, less than)
* Language (exact, icontains)<br>

**Example request**:<br> https://molodkina-books.azurewebsites.net/books/?Language__icontains=en&YearOfPublication__gt=1991

### GET /authors/{author_id}
**Description:** Returns a specific author based on Author ID.<br>
**Returns Values:**
* Author_id
* Name
* YearOfBirth
* YearOfDeath
* PlaceOfBirth
* PlaceOfDeath<br>

**Example request:** https://molodkina-books.azurewebsites.net/authors/2<br>

### GET /authors/{author_id}/books
**Description:** Returns an array of all books for a specific author.<br>
**Returns Values:**
* Book_id
* Title
* YearOfPublication
* Language
* Author_id<br>

**Example request:** https://molodkina-books.azurewebsites.net/authors/2/books<br>

### GET /authors/{author_id}/books/{book_id}
**Description:** Returns a specific book written by a selected author based on Book ID.<br>
**Returns Values:**
* Book_id
* Title
* YearOfPublication
* Language
* Author_id<br>

**Example request:** https://molodkina-books.azurewebsites.net/authors/2/books/5<br>

### GET /authors/{author_id}/countries
**Description:** Returns an array of all countries a selected author resided in over the course of his life.<br>
**Returns Values:**
* Country_id
* Name<br>

**Example request:** https://molodkina-books.azurewebsites.net/authors/2/countries<br>
