# Books

## Objectives

* Become more comfortable with Python.
* Gain experience with Flask.
* Learn to use SQL to interact with databases.

## What you need to find out

How to:

* set up and use PostgreSQL
* read and write JSON
* design and load a database
* use object-relational mapping (ORM) to interact with the database
* interface with someone's published API

## Overview

In this project, you'll build a book review website. Users will be able to
register for your website and then log in using their username and password.
Once they log in, they will be able to search for books, leave reviews for
individual books, and see the reviews made by other people.
You'll also use a third-party API by [openlibrary.org](https://openlibrary.org)
to pull in detailed information for each book, such as descriptions and cover images.

<!-- ## Preparations

Before your do anything else, watch and understand these video lectures:

- Lecture 2, [Flask](/lectures/flask)
- Lecture 3, [SQL](/lectures/sql)
- Lecture 4a, [APIs](/lectures/apis) (you can watch this later in the assignment)

If you have any questions about the lectures, please post a question! -->

## Bootstrapping

<!-- ### GitHub Classroom

We’ll again use GitHub Classroom to distribute projects and collect submissions. To begin Project 1:

1. [Click here](https://classroom.github.com/a/gj0uwP51) to go to the GitHub Classroom page for starting the assignment.
2. Click the green "Accept this assignment" button. This will create a GitHub repository for your project. Recall that a git repository is just a location where your code will be stored and which can be used to keep track of changes you make to your code over time.
3. Click on the link that follows "Your assignment has been created here", which will direct you to the GitHub repository page for your project. It may take a few seconds for GitHub to finish creating your repository.
4. Now, you should be looking at a GitHub repository titled uva-webapps/books-username, where username is your GitHub username. This will be the repository to which you will push all of your code while working on your project.
5. Submit the link to your project's GitHub repository below.

> This time, your git repository doesn't have a `gh-pages` branch, but a default `master` branch instead. This is because GitHub can't host websites created with Flask. For now, you'll just run your website locally, on your own computer. Later, you might choose to host your website online, for other people to see! -->

### PostgreSQL

For this project, you will need to set up a PostgreSQL database to use with your
application. PostgreSQL is designed to run as a stand-alone service (a seperate running program on your machine or perhaps on a server) that an app can interface with. First you will need to download and install PostgreSQL, here's how to do that:

* **On a Mac with [homebrew](https://brew.sh/)** simply run `brew install postgresql`. Just for reference: <https://wiki.postgresql.org/wiki/Homebrew>
* **On WSL on Windows** follow these instructions: <https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-database#install-postgresql>

Once installed, you need to run postgresql:

* **On a Mac with homebrew** run: `brew services start postgresql`
* **On WSL on Windows** run: `sudo service postgresql start`

These commands will launch PostgreSQL in the background. If you want to stop the program, just replace the word `start` with `stop` in the command above.

If perhaps familiar, like SQLite, PostgreSQL comes with its own command-line interface: `psql`. Once PostgreSQL is up and running, simply type `psql postgres` and you should then see your prompt change to `postgres=#`. From here you can try out queries, look at various databases, tables and their structures. The `psql` specific commands are different from SQLite, but here's a useful list to get you started: <https://www.geeksforgeeks.org/postgresql-psql-commands/>.

By default PostgreSQL will create a few empty databases to get you started called: `postgres`, `template0` and `template1`. By executing `psql postgres` we have opened `psql` in the `postgres` database. But instead, let's create our own database called `books`. To do this, inside `psql` execute:

    CREATE DATABASE books

Then **connect** to the new database with:

    \c books

All right, that is PostgreSQL all set up with a new fresh database called `books`.

### Flask

Let's get started with bootstrapping Flask. 

First open a terminal, then `cd` to a directory where you want to put your project.


    $ curl -LO https://github.com/minprog/project/raw/2022/flask/books/books.zip
    $ unzip books.zip
    $ rm books.zip
    $ cd books
    $ ls
    app.py  books.csv requirements.txt

Run

    $ pip3 install -r requirements.txt

to make sure all of the necessary Python packages (Flask and SQLAlchemy, for instance) are installed.

<!-- Run

    $ export FLASK_APP=app.py

to the environment variable `FLASK_APP` to be `application.py`. -->

<!-- You may optionally want to set the environment variable `FLASK_DEBUG` to `1`, which will activate Flask's debugger and will automatically reload your web application whenever you save a change to a file. -->

Set the environment variable `DATABASE_URL` to be the URI of your database. Here's how to that:

* `export DATABASE_URL="postgresql://localhost/books"` 

Run `flask run` to start up your Flask application.
If you navigate to the URL provided by `flask`, you should see the text
   `"Project 1: TODO"`!

### openlibrary.org API

[`openlibrary.org`](https://openlibrary.org) is an open library catalog. It tries to keep track of every published book. Perhaps most importantly for us, it exposes a free to use API. Allowing us to build on top of their work. See <https://openlibrary.org/developers/api> for all what is available.

In particular you are going to use the `Covers API` to retrieve cover images for books. All the details are here: <https://openlibrary.org/dev/docs/api/covers>

And the `Books API` to retrieve detailed descriptions for each book. See <https://openlibrary.org/dev/docs/api/books> for the documentation. You can test endpoints for the API by either navigating to them in your browser or by using `curl`. Often the documentation will come with examples for you to run.

Ultimately you will need to call endpoints for these API's from within `Flask`. Luckily there is a handy little library for that called: `requests`. If you have run `pip install -r requirements.txt` earlier, you should now have `requests` installed, and you can use it like so:

        import requests
        res = requests.get("https://openlibrary.org/api/books?bibkeys=ISBN:9780980200447&jscmd=details&format=json")
        json_data = res.json()
        print(json_data)

> Note that the above assumes the endpoint returns data in a `json` format.


## Requirements

Boots are strapped, it's time to actually build your web application! Here are the
requirements:

* **Registration**: Users should be able to register for your website, providing
  (at minimum) a username and password.
* **Login**: Users, once registered, should be able to log in to your website
  with their username and password.
* **Logout**: Logged in users should be able to log out of the site.
* **Import**: Provided for you in this project is a file called `books.csv`,
  which is a spreadsheet in CSV format of 5000 different books.
  Each one has an ISBN number, a title, an author, and a publication year.
  In a Python file called `import.py` separate from your web application,
  write a program that will
  take the books and import them into your PostgreSQL database. You will first need to
  decide what table(s) to create, what columns those tables should have, and how
  they should relate to one another. Run this program by running
  `python3 import.py` to import the books into
  your database, and submit this program with the rest of your project code.
* **Search**: Once a user has logged in, they should be taken to a page where
  they can search for a book. Users should be able to type in the ISBN number of
  a book, the title of a book, or the author of a book. After performing the
  search, your website should display a list of possible matching results, or
  some sort of message if there were no matches. If the user typed in only part
  of a title, ISBN, or author name, your search page should find matches for
  those as well!
* **Book Page**: When users click on a book from the results of the search page,
  they should be taken to a book page, with details about the book: its title,
  author, publication year, ISBN number, and any reviews that users have left
  for the book on your website.
* **Review Submission**: On the book page, users should be able to submit a
  review: consisting of a rating on a scale of 1 to 5, as well as a text
  component to the review where the user can write their opinion about a book.
  Users should not be able to submit multiple reviews for the same book.
* **Goodreads Review Data**: On your book page, you should also display (if
  available) the average rating and number of ratings the work has received from
  Goodreads.
* **API Access**: If users make a GET request to your website's `/api/<isbn>`
  route, where `<isbn>` is an ISBN number, your website should return a JSON
  response containing the book's title, author, publication date, ISBN number,
  review count, and average score (on your site). The resulting JSON should follow the format:

        {
            "title": "Memory",
            "author": "Doug Lloyd",
            "year": 2015,
            "isbn": "1632168146",
            "review_count": 28,
            "average_score": 5.0
        }

  If the requested ISBN number isn't in your
  database, your website should return a 404 error.
* You should be using raw SQL commands (as via SQLAlchemy's `execute` method) in
  order to make database queries. You should not use the SQLAlchemy ORM (if
  familiar with it) for this project.
* In `README.md`, include a short writeup describing your project, what's
  contained in each file, and (optionally) any other additional information the
  staff should know about your project.
* If you've added any Python packages that need to be installed in order to run
  your web application, be sure to add them to `requirements.txt`!

Beyond these requirements, the design, look, and feel of the website are up to
you! You're also welcome to add additional features to your website, so long as
you meet the requirements laid out in the above specification!

## Hints

- [Adminer](https://adminer.cs50.net) can be user to try out SQL-statements.
- At minimum, you'll probably want at least one table to keep track of users,
  one table to keep track of books, and one table to keep track of reviews. But
  you're not limited to just these tables, if you think others would be helpful!
- In terms of how to "log a user in," recall that you can store information
  inside of the `session`, which can store different values for different users.
  In particular, if each user has an `id`, then you could store that `id` in the
  session (e.g., in `session["user_id"]`) to keep track of which user is
  currently logged in.
- When adding any files like pictures or JavaScript, make sure you place them in
     the `static` folder. ([documentation](http://flask.pocoo.org/docs/1.0/tutorial/static/))


## FAQs

#### `INSERT`-statements do not work, but aren't giving an error?

Make sure you commit you changes with `db.commit()`.

#### For the API, do the JSON keys need to be in order?

Any order is fine!

#### `AttributeError: 'NoneType' object has no attribute '_instantiate_plugins'`

Make sure that you've set your `DATABASE_URL` environment variable before running
`flask run`!


## How to Submit

You should have submitted the link to your generated repository already when starting!

Example: `https://github.com/uva-webapps/books-username`