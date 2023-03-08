# Books

## Objectives

* Become more comfortable with Python and Flask.
* Learn to use SQL and ORMs to interact with databases.
* Learn to interface and build upon public APIs.

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

Once installed, you need to run PostrgreSQL:

* **On a Mac with homebrew** run: `brew services start postgresql`
* **On WSL on Windows** run: `sudo service postgresql start`

These commands will launch PostgreSQL in the background. If you want to stop the program, just replace the word `start` with `stop` in the command above.

If perhaps familiar, like SQLite, PostgreSQL comes with its own command-line interface: `psql`. Once PostgreSQL is up and running, simply type `psql postgres` and you should then see your prompt change to `postgres=#`. From here you can try out queries, look at various databases, tables and their structures. The `psql` specific commands are different from SQLite, but here's a useful list to get you started: <https://www.geeksforgeeks.org/postgresql-psql-commands/>.

By default PostgreSQL will create a few empty databases to get you started called: `postgres`, `template0` and `template1`. By executing `psql postgres` we have opened `psql` in the `postgres` database. But instead, let's create our own database called `books`. To do this, inside `psql` execute:

    CREATE DATABASE books;

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
    README.md books.csv requirements.txt
    app.py    models.py

Run

    $ python3 -m pip install -r requirements.txt

to make sure all of the necessary Python packages (Flask and SQLAlchemy, for instance) are installed.

<!-- Run

    $ export FLASK_APP=app.py

to the environment variable `FLASK_APP` to be `application.py`. -->

<!-- You may optionally want to set the environment variable `FLASK_DEBUG` to `1`, which will activate Flask's debugger and will automatically reload your web application whenever you save a change to a file. -->

Set the environment variable `DATABASE_URL` to be the URI of your database. Here's how to that:

    export DATABASE_URL="postgresql://localhost/books"

Run `flask run --debug` to start up your Flask application.
If you navigate to the URL provided by `flask`, you should see the text
   `"Project 1: TODO"`!

### openlibrary.org API

[`openlibrary.org`](https://openlibrary.org) is an open library catalog. It tries to keep track of every published book. Perhaps most importantly for us, it exposes a free to use API. Allowing us to build on top of their work for free. See <https://openlibrary.org/developers/api> for all that is available to us.

In particular you are going to use the `Covers API` to retrieve cover images for books. All the details are here: <https://openlibrary.org/dev/docs/api/covers>

And the `Books API` to retrieve detailed descriptions for each book. See <https://openlibrary.org/dev/docs/api/books> for the documentation. You can test endpoints for the API by either navigating to them in your browser or by using `curl`. Often the documentation will come with examples for you to run.

Ultimately you will need to call endpoints for these API's from within `Flask`. Luckily there is a handy little library for that called: `requests`. If you ran `pip install -r requirements.txt` earlier, you should now have `requests` installed, and you can use it like so:

    import requests
    res = requests.get("https://openlibrary.org/api/books?bibkeys=ISBN:9780980200447&jscmd=details&format=json")
    json_data = res.json()
    print(json_data)

Or alternatively, and perhaps a little easier to read:

    import requests
    res = requests.get("https://openlibrary.org/api/books", params={
      "bibkeys": "ISBN:9780980200447",
      "jscmd": "details",
      "format": "json"
    })
    json_data = res.json()
    print(json_data)

> Note that the above assumes the endpoint returns data in a `json` format.


## Requirements

Boots are strapped, it's time to actually build your web application! Here are the
requirements:

#### Features:

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
* **Registration**: Users should be able to register for your website, providing
  (at minimum) a username and password.
* **Login**: Users, once registered, should be able to log in to your website
  with their username and password.
* **Logout**: Logged in users should be able to log out of the site.
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
* **Cover and Descriptions**: On your book page, you should also display (if
  available) the cover and description retrieved from the openlibrary.org API.
* **API Access (optional)**: If users make a GET request to your website's `/api/<isbn>`
  route, where `<isbn>` is an ISBN number, your website should return a JSON
  response containing the book's title, author, publication date, ISBN number,
  description, and cover URL. The resulting JSON should follow the format:

        {
            "title": "Memory",
            "author": "Doug Lloyd",
            "year": 2015,
            "isbn": "1632168146",
            "description": "",
            "cover_url": ""
        }

  If the requested ISBN number isn't in your database, your website should return a 404 error.

#### Technical requirements

* You should use the SQLAlchemy ORM for this project. Any models should live a file called `models.py`.
* In `README.md`, include a short writeup describing your project, what's
  contained in each file, and (optionally) any other additional information the
  staff should know about your project.
* If you've added any Python packages that need to be installed in order to run
  your web application, be sure to add them to `requirements.txt`!

> Beyond these requirements, the design, look, and feel of the website are up to you! You're also welcome to add additional features to your website, so long as you meet the requirements laid out in the above specification!

## Walkthrough

This assignment starts with relatively little starter code. This means you will have to put most of the puzzle pieces together yourself. Luckily the lecture arms you with working examples of similar challenges that you will face while working on this assignment. So be sure to keep the lecture at hand, and to [TODO DOWNLOAD URL]() the examples.

There is a lot to do, and you can work through it all in a different order, but here's our advice:

#### Step 1: import.py

Start with setting up the database by implementing `import.py` (and `models.py` and `create.py`). Ultimately `import.py` should fill the database with book data from `books.csv`. To do this, recall the flights example from lecture that posed a similar challenge albeit on a different topic. 

1. First, Brian introduced `create.py` to create the database based on models from `models.py`. We suggest you start by copying these files from lecture.
2. Then change `models.py` to no longer have a `Flight` and `Passenger` model, but a `Book` model instead. No need to worry about users and reviews just yet. Take a closer look at `books.csv` to figure out what a `Book` should consist of.
3. Go ahead and run `create.py`. If all goes well, run `psql books` and then `\dt` to see the newly created table.
4. For `import.py` copy and rename `import1.py` from lecture. 
5. Then modify `import.py` to read in `books.csv` instead of `flights.csv`, and write all books data to the database.

#### Step 2: book page

With the books in the database, start by implementing a simple version of the **book page**. In the final version this page will render reviews and cover images, but for now let us focus on displaying just what is in our database.

1. Head on over to `app.py` and add the following route:
    
        @app.route("/book/<isbn>", methods=["GET"])
        def book(isbn):
            # TODO

    Notice how this is a parameterized route. The `<isbn>` part in the route signals to flask that a user should navigate to `/book/` followed by something else (presumably an isbn). Whatever follows `/book/` is then passed as an argument to the `book` function, conveniently named `isbn` also. The idea of this route being that navigating to say `/book/1632168146` gives you the page on the book with `1632168146` as its isbn.
2. Create a `templates` directory and add a template for the book page. Then have the `/books/<isbn>` route render it. Don't invest too much effort into styling and layout just yet. You can test this route by running your app with `python3 -m flask run --debug` and then navigating over to `127.0.0.1:5000/book/1632168146` in your browser.
3. Now add the necessary logic to the `/books/<isbn>` route to get the book with the right isbn from the database. Then pass on that book to the template and have the template render the title, isbn, etc. Take another look at the flights example from the lecture for this part.
4. Finally, handle the "wrong path". What do you do if the book with that specific `isbn` is not in your database?

#### Step 3: users

Next up is registering and login for users. For this it is best to look back at the Finance assignment. You will find that most code of that assignment concerning users and login is reusable for this assignment, with a few caveats.

1. In contrast to Finance, we are now working with an ORM. So the first task is to set up a `User` model in `models.py`. Then once you have done so, don't forget to rerun `create.py` to create the database table for users.
2. Next, copy over the code for the `/login` and `/register` routes to `app.py`. Odds are you will want to reuse the `@login_required` decorater as well. To do this, copy `helpers.py` from Finance and import `login_required` in `app.py`.
3. Copy over or create templates for the login and register page. Again, don't worry about aesthetics too much just yet. 
4. The `/login` and `/register` routes from Finance work with raw SQL queries. It is up to you to transform these to work with the ORM instead. Tackle one route at a time, and remember to test your work by navigating to the routes yourself and by inspecting the database. For instance, you might want to run `psql users` and `SELECT * FROM users`. That is, assuming you have called your table `users`. 

> Do not store passwords in plaintext! Instead, like in Finance, use `check_password_hash` and `generate_password_hash` from `werkzeug.security`. You can import these functions like so: `from werkzeug.security import check_password_hash, generate_password_hash`.

#### Step 4: search

Now we need some method to discover books. Something a bit more user friendly than directly typing in the isbn in the browser's URL bar. So let's start working on the search page.

1. Create a template for the search page and add a route to `app.py`.
2. The search page will need a form to search with. For inspiration, check out the `index.html` template from lecture. Go ahead and add a search form to your template.
3. Now add the necessary logic to your search route in `app.py` to search the database. Per the requirements you will need to support search for isbn, title, author, or any part of them. No need to worry about combinations, but do feel free to challenge yourself. Be sure to check your work every now and again while working on this step. Even though you might not have a template to render results just yet, you can still print out any matching books to the terminal by simply calling `print()` in `app.py`.
4. Extend the search template with a list or a table to display the results of the search if any. We recommend this method over introducing another template as this way the user can keep searching without having to navigate to a new page. For inspiration check out the `flights.html` template from lecture.
5. Finally, make sure that a user can click on any book in the search results to take them to that book's page.

> The lecture introduces `like` as a method to search for similar results "like" the query. Odds are you will find `ilike` helpful for this step. It operates the same as `like`, just case insensitive.


#### Step 5: descriptions and book covers

`books.csv` contains a sizeable number of books, but has quite limited information on each book. This makes for a rather dull book page. So let us build on the shoulders of giants and use online resources to extend our book page.

1. First up, let's add books covers to the book page. For this [openlibrary.org](https://openlibrary.org) provides a helpful little Cover API over at <https://openlibrary.org/dev/docs/api/covers>. All the instructions on the API and how to use it are on that page.
2. Next, let's add descriptions to the book page through openlibrary.org's Book API over at <https://openlibrary.org/dev/docs/api/books>. This API is a bit more involving than the covers API. For this part you will ultimately need to call an endpoint of the API from within `app.py`, extract the description from the API call's response, and then pass that description on to the book's template. First take a minute to look at the API's docs and especially the example all the way at the bottom with the following call:

        $ curl 'https://openlibrary.org/api/books?bibkeys=ISBN:9780980200447&jscmd=details&format=json'

    There are a couple of optional arguments in this API call:

    * bibkeys=ISBN:9780980200447
    * jscmd=details
    * format=json

    From the API docs, try to understand what each of these arguments does, and why we need/want them.

3. Lets move the API call from the example to `app.py`. Be sure to `import requests` then add the following code to your books route:
    
        response = requests.get("https://openlibrary.org/api/books?bibkeys=ISBN:9780980200447&jscmd=details&format=json")
        data = response.json()
        print(data)

4. The code above will send a get request to the API and await its response. Once that comes in, the json part of the response is parsed. The resulting dictionary is stored in a variable called `data` and printed. Now it is up to you to modify the API call to not always query for the book with isbn 9780980200447, and to extract the description from `data`. Once you have the description, pass it down to your book template and render it.


#### Step 6: reviews

Last up, add user interaction to the website through reviews. Per the requirements, a user should be able to leave just one review per book consisting of a rating and a text component. 

1. Reviews are a new thing we need to store in the database. This means you will have to introduce a new model to `models.py`. But, this model is different from the others as it is related to both users and books. Do check out the `models.py` from lecture again on how to model relationships between different tables through SQLAlchemy.
2. Next, extend the book template with a new form to leave a review. This form should minimally have some method of leaving a star rating and a text component.  
3. Introduce a route to `app.py` to handle the review form submit. Be sure to check that the user has not already submitted a review for this book before.
4. Finally, extend the book template again to render all reviews for that book and add the necessary logic to the book page route in `app.py`.


#### Additional features and improvements

At this point the website is functionally complete, but pretty rough looking and probably not all that user friendly. If you have time to spare, and want to challenge yourself further, try to:

* Extend the website with an API of your own. See the optional requirement above.
* Allow users to update and remove reviews.
* Add a section for highly user-rated books.
* Fix the navigation on the website, allow users to traverse to recently visited books.
* Rank (order) the search results in a user friendly fashion.
* Polish up the easthetics.
* Break up larger templates in smaller reusable templates.
* Enable user moderation through a voting or flagging system on reviews.
* ...


## Hints

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

#### `INSERT`-statements do not work and do not give an error?

Make sure you commit you changes with `db.commit()`.

#### For the API, do the JSON keys need to be in order?

Any order is fine!

#### `AttributeError: 'NoneType' object has no attribute '_instantiate_plugins'`

Make sure that you've set your `DATABASE_URL` environment variable before running
`flask run`!


## How to Submit

You should have submitted the link to your generated repository already when starting!

Example: `https://github.com/uva-webapps/books-username`