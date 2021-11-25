# Commerce: Design Document


## Understanding

In the distribution code is a Django project called `commerce` that contains a single app called `auctions`.

First, open up `auctions/urls.py`, where the URL configuration for this app is defined. Notice that we've already written a few URLs for you, including a default `index` route, a `/login` route, a `/logout` route, and a `/register` route.

Take a look at `auctions/views.py` to see the views that are associated with each of these routes. The index view for now returns a mostly-empty `index.html` template. The `login_view` view renders a login form when a user tries to GET the page. When a user submits the form using the POST request method, the user is authenticated, logged in, and redirected to the `index` page. The `logout_view` view logs the user out and redirects them to the `index` page. Finally, the `register` route displays a registration form to the user, and creates a new user when the form is submitted. All of this is done for you in the distribution code, so you should be able to run the application now to create some users.

Run `python manage.py runserver` to start up the Django web server, and visit the website in your browser. Click "Register" and register for an account. You should see that you are now "Signed in as" your user account, and the links at the top of the page have changed. How did the HTML change? Take a look at `auctions/templates/auctions/layout.html` for the HTML layout of this application. Notice that several parts of the template are wrapped in a check for if `user.is_authenticated`, so that different content can be rendered depending on whether the user is signed in or not. You're welcome to change this file if you'd like to add or modify anything in the layout!

Finally, take a look at `auctions/models.py`. This is where you will define any models for your web application, where each model represents some type of data you want to store in your database. We've started you with a `User` model that represents each user of the application. Because it inherits from `AbstractUser`, it will already have fields for a username, email, password, etc., but you're welcome to add new fields to the User class if there is additional information about a user that you wish to represent. You will also need to add additional models to this file to represent details about auction listings, bids, comments, and auction categories. Remember that each time you change anything in `auctions/models.py`, you'll need to first run `python manage.py makemigrations` and then `python manage.py migrate` to migrate those changes to your database.



## Creating a design document

Your first to-do is to read the project specification in full and try to imagine what the website will look like. Then, create a design document that describes **what** you are going to make and what it will look like. While doing this, there are also some technical challenges that you need to take into account as much as possible.

For this project, we would like you to take the items below as a guide for producing design documentation:

- The project requirements describe the application **workflow**, the steps that users can take to reach certain goals. Use the descriptions of the workflow to make a complete sketch of all pages, including all user interface elements, with lines pointing from buttons toward pages that those buttons lead to.

- Analyse which **models** you're going to need, and create a [Class Diagram](https://www.visual-paradigm.com/guide/uml-unified-modeling-language/uml-class-diagram-tutorial/) specifying all of them. You can do this on paper or user an online tool like [diagrams.net](https://app.diagrams.net).

- The information from the database is needed on different pages. Make an overview of which pages will be using what information from the database.

You should put your lists and sketches in a separate folder in your GitHub repository and embed the pictures in your README.md for easy reference.


## Form

<div class="form-check">
  <input name="form[design_doc_done]" class="form-check-input" type="checkbox" value="yes" id="check1" required>
  <label class="form-check-label" for="check1">
    I have added a design document (as Markdown) to my repository as README.md in the root folder
  </label>
</div>

<div class="form-check">
  <input name="form[images]" class="form-check-input" type="checkbox" value="yes" id="check2" required>
  <label class="form-check-label" for="check2">
    I have added neat sketches of all pages in one or more images that are well-readable, and embedded those pictures in the design document using Markdown image tags
  </label>
</div>

<div class="form-check">
  <input name="form[images_dir]" class="form-check-input" type="checkbox" value="yes" id="check3" required>
  <label class="form-check-label" for="check3">
    I have put all images in a separate folder, not in the root folder
  </label>
</div>

<div class="form-check">
  <input name="form[discussed]" class="form-check-input" type="checkbox" value="yes" id="check4" required>
  <label class="form-check-label" for="check4">
    I have discussed my design with another student to get preliminary feedback and to check for completeness
  </label>
</div>

<div class="form-check">
  <input name="form[discussed]" class="form-check-input" type="checkbox" value="yes" id="check5" required>
  <label class="form-check-label" for="check5">
    I have pushed the Markdown to GitHub and checked that it is well-readable when navigating to it via the GitHub website
  </label>
</div>
