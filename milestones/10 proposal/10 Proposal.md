# Project Proposal

You'll kick off your project by handing in a proposal document. This document should connect the functional design of your project (what does it do?) to a problem in the real world. Below, we list all required aspects of your proposal document.

## Getting started

1. To start your project, you should accept a new assignment on GitHub classroom: [Final Project](https://classroom.github.com/a/xxwP7Upy). This will create a GitHub repository for your project.

2. Click on the link that follows "Your assignment has been created here", which will direct you to the GitHub repository page for your project. It may take a few seconds for GitHub to finish creating your repository.

Now, you should be looking at a GitHub repository titled `uva-webapps/project-username`, where `username` is your GitHub username. This will be the repository to which you will push all of your code while working on your project.

Inside your new repository you will find a mostly empty file called `README.md`. Your should write your proposal in that file using the **Markdown** language ([read a brief intro](https://guides.github.com/features/mastering-markdown/)).

## Adding pictures

You will need to include some sketches into your proposal. Put these images inside the folder called **doc** inside your repository. Use exactly that name, for consistency with other projects! To use pictures from the `doc` folder in a Markdown document, use the following example.

    ![Alternative Text](doc/image.png)

Make sure that you provide an alternative (descriptive!) text inside the square brackets as well, as this will greatly help visually impaired people in understanding the contents of your proposal, as well as guarantee that the content of the image is clear, even if it fails to load. 

## Goal of the document

You and others can use this document to estimate the effort required to implement the project. Your project has a high risk of failure if:

- the envisioned product tries to do too much
- the envisioned product doesn't do enough
- the purpose of the product is not well-defined (too vague)

By writing a clear proposal document and getting feedback on it from multiple students and teachers, you can better avoid these risks!

## Problem statement

Write a brief statement, four lines of text, about the **problem** (not the solution) that your finished product will solve or the idea that it is based on. The problem has to be clearly described and very specific. We see a few possibilities:

- There is a clearly defined problem that a reasonable group of people have, which a web application is particularly suited to solve.
- There is a widespread lack of knowledge or understanding that an interactive visualization or story is particularly suited to remedy.
- There is an interesting game concept that is particularly suited to implementing in a server-side or client-side web application.

In all cases, you should be able to define a specific target audience or a specific categorization of your proposed web application. Include that, too.

## Solution sketch

Describe your solution in moderate detail. You are sketching the "user experience": the situation that a user might be in and of which using your website is a part.

> You should not use a formal sketching app (like a "wireframing" tool). Doing that will be part of your next step. For now, draw by hand, doodle a little bit, throw away, start again and finally draw your basic sketch by hand. The idea is that you do not spend too much time on details in this phase, but just enough for someone to decide if your project is "enough".
{:.bg-light}

- **Summarize** your idea in one or two sentences, connecting it to the problem that you have defined. "This application will..."

- Include a **visual sketch** of what the final product will look like for the user; if you envision the application to have multiple screens, sketch these all out separately. Clearly specify the possible user interactions (click on button, move to next page), and include concrete examples of contents. Your sketches have to be complete and neat!

	![embed](https://www.youtube.com/embed/j0vP77s_bXc)

- Use a good tool to photograph your sketch and convert to a good quality picture to embed into your proposal. You can also split up your sketch in multiple parts that you separately embed.

- If your sketches are unreadable, or you've put them sideways, or is missing obviously needed screens, your proposal will not (yet) be looked at. This will delay your project and you will need to compensate for that. In other words: take the time to draw good sketches.


## Prerequisites

Describe the things that you'll have to get in order before really starting your project. You should do this based on what you know **now**. After submitting you proposal document, during feedback conversations with other students, or with teachers, additional stuff may come up. You may add those things to your proposal at that time.

- List any **data sources** that you will use and whether you will need to transform the data before it is usable for your application. The list should include links to where the data sources can be found (downloaded or accessed via API). If you need to have an account to access the data, make the account now. Often it proves to be harder than expected to access good data.

- List the **external components** (libraries like `sqlalchemy` or `bootstrap`) that you need to implement certain features. Include the names, and if the component is not very standard, include a link to its website. Specify what part you need and what for.

- Include a review of **similar** web apps, in terms of features and technical aspects: what do they do? how have they implemented it? can you do it in the same way? (Spend a few lines per "competitor".)

- Identify the **hardest parts** of implementing your application: think of technical problems or limitations that could arise during development and what possibilities you have to overcome these.

## Sanity check

Before continuing, compare your solution to the project requirements one last time. Also, is it still clear that your proposed project is indeed a solution to the stated problem?

The proposal document should be well-written and clearly formatted. Do not forget to include a
title, your name, and a paragraph summary of the application goals at the top. Use Markdown to format your headers etc.

Finally, make sure that your document is spell-checked, and that images are **not too large** or too small (your document will be read in a normal browser via GitHub).

## Submitting

After you have pushed all changes to Github, copy the URL of the GitHub page for your project and submit it below. It will be in this format: `https://github.com/uva-webapps/final-username`.

Don't commit any **code** yet, just your proposal. Your repository should be clean for us to read, containing the `README.md`, a `doc` folder, pictures in the `doc` folder, an empty `app` folder and nothing else.

## What's next

The next step in your project is creating a design document. There, you'll describe how your project will be created according to the rules of the application framework that you're using.

Meanwhile, keep an eye on the **GitHub Issues** for your project (go to your repo webpage on the GitHub site and then go to Issues). This is where you will get feedback on whether your project is accepted as it is described, or you need to make some changes.

## Submit

Below, you submit your GitHub repo URL. In addition, make sure you check off these points:

<div class="form-check">
  <input name="form[readme]" class="form-check-input" type="checkbox" value="yes" id="check1">
  <label class="form-check-label" for="check1">
    My repository only contains a README.md document, no code
  </label>
</div>

<div class="form-check">
  <input required name="form[doc]" class="form-check-input" type="checkbox" value="yes" id="check2">
  <label class="form-check-label" for="check2">
    My repository contains the required pictures in a separate "doc" folder
  </label>
</div>

<div class="form-check">
  <input required name="form[markdown]" class="form-check-input" type="checkbox" value="yes" id="check3">
  <label class="form-check-label" for="check3">
    README.md is written in good Markdown with headings, lists, pictures etc.
  </label>
</div>

<div class="form-check">
  <input required name="form[listofdatasources]" class="form-check-input" type="checkbox" value="yes" id="check4">
  <label class="form-check-label" for="check4">
    README.md contains links to data sources and concrete examples of the data that's needed
  </label>
</div>

<div class="form-check">
  <input required name="form[listofcomponents]" class="form-check-input" type="checkbox" value="yes" id="check5">
  <label class="form-check-label" for="check5">
    README.md contains a global list of needed components other than Flask, SQL and Javascript
  </label>
</div>

<div class="form-check">
  <input required name="form[listofotherapps]" class="form-check-input" type="checkbox" value="yes" id="check6">
  <label class="form-check-label" for="check6">
    README.md contains multiple examples of similar apps and describes what my app does differently
  </label>
</div>

<div class="form-check">
  <input required name="form[listofhardtofigureout]" class="form-check-input" type="checkbox" value="yes" id="check7">
  <label class="form-check-label" for="check7">
    README.md contains a small list of things that I think will take most time to figure out/implement
  </label>
</div>
