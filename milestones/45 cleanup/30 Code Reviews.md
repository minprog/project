# Cleanup

Je **code** staat al vast, maar je **repository** is nog niet netjes en volledig. Dit ga je vandaag verbeteren. Deze verbeteringen kun je vervolgens committen en pushen naar je repository op GitHub (geen nieuwe code, wel andere dingen).

## Deel 1: code review

> De review wordt meegenomen in de beoordeling van het **code**-deel van je projectcijfer. Je mag je code niet meer aanpassen, maar in de review kun je laten zien dat je het wel beter had kunnen doen als je nog veel meer tijd had (en hoe je dat dan zou moeten doen!).

Doel van de code reviews is niet om je code nog te verbeteren, maar om te reflecteren op de kwaliteit van je eigen code. Je krijgt hierbij hulp van een andere student.


1. Pick a partner.

2. Open your project on your computer and put your partner in front of it. Your partner should navigate the code, not you!

3. Your partner will now comment (aloud!) on your code. You will listen. If there are questions, answer them. Make note of those questions: this may be where your project could be better documented, or where your code could be more clear!

The reviewer must pay attention to:

- How easy it is to make sense of the complete code base (can you understand what goes where and why?). Think aloud when doing this, so the coder under review can take notes and make their code better.

- Stylistic issues in the code. Make sure that you point out the weak spots.

Het resultaat van de review plaats je in `REVIEW.md`. Naar verwachting zijn dit wel gemiddeld 5 flinke verbeterpunten die je uitgebreid kunt beschrijven, maar dat ligt natuurlijk helemaal aan de code!

Schrijf bovenaan de file de naam van de student die jouw geholpen heeft met de review.

## Deel 2: cleanup

> De "netheid" van je repository wordt meegenomen in de beoordeling van het **repository**-deel van je eindcijfer.

### Updating the README

Your GitHub repository should contain a complete `README.md` file that states the application name, one or two screen shots (**resized** to small width/height), a description of the app's purpose, and your name. The `README` should be easy to read and give a quick overview.


### Updating your design document

The `DESIGN.md` should still be in the root of your repository, next to the `README.md`. You should update it to provide a high-level technical overview of your app as it is now. Things we'll look for:

- To understand a web app, it's nice to start at the routes/URLs. However, there may be many and the purpose may not immediately be clear. In your `DESIGN`, provide tiny screenshots of the main functions (screens/interactions) of the app, and for each:

    - describe which file implements that functionality (if needed),
    - provide a list of which routes/URLs are connected to what functionality,
    - describing the task that each route performs.

- List other parts that should be looked at.

In general, do not present all info in one big list, but instead try to present the information clearly for someone who doesn't quite know your project.

### Adding ASSESSMENT.md

Take a look at the [syllabus](/syllabus) to see how your project will be assessed. In `ASSESSMENT.md` you should make a simple list of thing that you do not want us to miss when grading! Clearly point us to things in your code that you particularly like, or describe how you cleaned up certain parts, or parts of the functionality of the app that you're particularly proud of. You should expect that we take all of your code and functionality into account for grading, not just what you list here, but we surely do not want to miss those best parts!

Also, choose the biggest decisions you've taken during the project, from your `PROCESS.md` and write about those: why did you make the decision, what was bad about the previous design ideas, why is the new solution better (and is it still better, now that your project is finished?). A small paragraph, like this one, per big decision suffices.

### Choosing a license for your work

A copyright statement can be either:

- a *public domain* release, which releases your code to the public without any restrictions (you could also use the *unlicense* for this, see below)

- a *copyright notice* which states who actually owns the rights to the materials in the repository (probably only you)

Copyright is automatic in the Netherlands: if you create something, you own the copyright, but you can release your code to the public domain by stating so in (for example) the `README` file.

If you do want to retain copyright, which is common, then you should note the copyright including the current year, followed by "Alle rechten voorbehouden" or "All rights reserved". This clause means that you will not allow copying, modification, distribution etc.

Even if you claim "All rights reserved," you can add a more liberal license to that, allowing some ways of sharing or modification. This is common for open source projects. If you're proud of your code and want other people to share, you might add an open source license. Anyone who finds your project on GitHub can see that you're fine with sharing!

Follow directions at [GitHub help](https://help.github.com/articles/adding-a-license-to-a-repository/) to add a `LICENSE` file and choose a license that you like, unless you retain all rights for yourself.

### Adding acknowledgements

The `README` should also acknowledge sources of external code, images and other materials that are in the repository but not created by yourself. Make sure that it is clear which directories are copyrighted by different creators.

You do not have to credit authors of small code snippets (for example, from Stack Overflow) in your `README`. Instead, you should have added a small comment near the snippet, right in your code. You do not have to credit the teachers, who are happy to have helped you, but do not claim copyright for their contributions :-)

**Don't forget to push all changes!**
