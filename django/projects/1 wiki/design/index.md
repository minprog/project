# Wiki: Design Document

From now on, we require that you take your time to do a formal up-front design of what you are going to make for this project.


## Understanding

In the distribution code is a Django project called `wiki` that contains a single app called `encyclopedia`.

First, open up `encyclopedia/urls.py`, where the URL configuration for this app is defined. Notice that we've started you with a single default route that is associated with the `views.index` function.

Next, look at `encyclopedia/util.py`. You won't need to change anything in this file, but notice that there are three functions that may prove useful for interacting with encyclopedia entries. `list_entries` returns a list of the names of all encyclopedia entries currently saved. `save_entry` will save a new encyclopedia entry, given its title and some Markdown content. `get_entry` will retrieve an encyclopedia entry by its title, returning its Markdown contents if the entry exists or `None` if the entry does not exist. Any of the views you write may use these functions to interact with encyclopedia entries.

Each encyclopedia entry will be saved as a Markdown file inside of the `entries/` directory. If you check there now, you'll see we've pre-created a few sample entries. You're welcome to add more!

Now, let's look at `encyclopedia/views.py`. There's just one view here now, the `index` view. This view returns a template `encyclopedia/index.html`, providing the template with a list of all of the entries in the encyclopedia (obtained by calling `util.list_entries`, which we saw defined in `util.py`).

You can find the template by looking at `encyclopedia/templates/encyclopedia/index.html`. This template inherits from a base `layout.html` file and specifies what the page's title should be, and what should be in the body of the page: in this case, an unordered list of all of the entries in the encyclopedia. `layout.html`, meanwhile, defines the broader structure of the page: each page has a sidebar with a search field (that for now does nothing), a link to go home, and links (that don't yet work) to create a new page or visit a random page.


## Creating a design document

Your first to-do is to read the project [specification](/django/projects/wiki/specification) in full and try to imagine what the website will look like. Then, create a design document that describes **what** you are going to make and what it will look like. While doing this, there are also some technical challenges that you need to take into account as much as possible.

For this project, we would like you to take the items below as a guide for producing design documentation:

- The project comes with a number of files already. Say you are going to add a **new page**, what files should you change to make that work?

- An important part of the project is creating HTML files for some of the pages. Make a list of the HTML pages that you are going to need. Don't forget to add any pages that would be needed but aren't directly mentioned in the project requirements.

- The project requirements describe the application workflow, the steps that users can take to reach certain goals. Use the descriptions of the workflow to make a complete sketch of all pages, including all user interface elements, with lines pointing from buttons toward pages that those buttons lead to.

One brief introduction for that last item is the [Beginner's guide to UI sketching](https://www.justinmind.com/blog/ui-sketching/) at JustInMind. Read it well!

You should put your sketches in a **separate** folder inside your GitHub repository for Wiki, so you can discuss these with your mentor before starting coding!


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
