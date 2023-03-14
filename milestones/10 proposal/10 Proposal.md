# Proposal

We start with a project proposal. That is a document that connects the functional design of the project to a real world problem. Essentially, what does it do to address something real. Below are the required aspects of the proposal.

## Purpose of this document

Projects inherently have some risk of failure, and there are certain signs that indicate a high risk:

- The project tries to do too much or too little.
- The goal is very vaguely defined.
- It is unclear who would (want to) use the product.
- The problem the project adresses does not exist or is already solved.

The overarching theme here is, the clearer your vision on what the project should be by course's end, the higher the chance of success. Mind you, success here is a good finished project. By no means does it need to be a popular or commercial success. 

There are steps you can take to greatly increase the chance of success. A lot of it is in preperation and getting feedback from fellow students and the staff. Take the time to work on your proposal. While working on it, talk to others about your ideas and ask for feedback!

## Some questions

In your proposal answer the following questions with a few lines of text. That is, if the question is relevant to your specific project.

1. What is **the problem** (not the solution) that the project will solve? Be clear and specific. For example:

- There is a clearly defined problem that a reasonable group of people faces. A web app is a welcome solution here.
- There is a broad lack of knowledge on a certain topic. An interactive visualization on storytelling app is missing here.
- There is a game concept that only exists in physical form. But in days of isolation this is impossible and it needs to be lifted to a web app.

2. Who are your projected users? Essentially, who are you building this project for. For example:

- Elderly people who are generally unfamiliar with the project's topic.
- People on the move.
- Power users only, they know the topic inside and out.
- The inhabitants of Lab42.
- Me, myself, and I.

3. What is or are the setting(s) that your application is used in? For example:

- On an always on big screen with no interaction. An admin handles configuration on a separate screen.
- Primarily used on the go, likely on a smaller device like a smart phone.
- On a laptop or desktop with a relatively big screen and keyboard available.

4. What does your solution do different or better than existing solutions? Essentially, what is your niche? For example:

- This app is customized for location/business/group. It solves specific needs and problems that location/business/group has, that a more general app does not solve.
- This solution focuses on a small part of a bigger problem, for which there is no good solution yet.

## Sketch your solution

Next, write and **draw** up your solution. Really, draw. This is perhaps the most important step in the entire process. Because once you start drawing things out, you start to discover what needs to exist. There are all these little pieces that you easiliy gloss over in text, but not so much in drawings.

What you do, depends a little on the type of project:

- If you are creating a user focused program, say a game or a web app, then sketch the user experience. In other words, the situation that a user finds themselves in:

    - Add sketches for how the finished product will look like for the user. If you need multiple screens or windows, sketch them individually. 
    - Make it clear how actions and navigation work in your app.
    - Add concrete examples of content. Don't just Lorum ipsum everywhere.

        ![embed](https://www.youtube.com/embed/j0vP77s_bXc)

    - Ensure your sketches give a complete overview. 

- If you are instead creating a tool or an algorithm to analyse data or do some form of prediction, then draw out the components of your solution. This depends on what you are building, but for instance in case of data processing you might sketch the various parts of a data processing pipeline. 

In all cases:

- Briefly summarize your solution (one or two sentences) and connect it to the problem you are trying to solve. "This app will...."

- Take a minute to find a good tool to photograph your drawings. A straight up good quality photo does make a significant difference. In either case make sure your drawings are legible. If we cannot reasonably read or comprehend what is there, it might delay the start of your project somewhat and that requires you to compensate later on in the course. You are also free to use some computer program for drawings and sketches, but generally we do recommend paper.

## Vereisten

Beschrijf ook de dingen die je op orde moet krijgen voordat je echt aan je project begint. Je moet dit doen op basis van wat je **nu** weet. Na het indienen van je projectvoorstel, tijdens feedbackgesprekken met andere studenten of met docenten, kunnen er extra dingen naar voren komen. Je kunt die zaken dan aan je voorstel toevoegen.

- Maak een lijst van alle **gegevensbronnen** die je gaat gebruiken en of je de gegevens moet transformeren voordat ze bruikbaar zijn voor de toepassing. De lijst moet links bevatten naar waar de gegevensbronnen te vinden zijn (gedownload of toegankelijk via een API). Als je een account nodig hebt om toegang te krijgen tot de gegevens, maak je het account nu aan. Vaak blijkt het moeilijker dan verwacht om toegang te krijgen tot goede data.

- Maak een lijst van de **externe componenten** (denk aan bibliotheken zoals `sqlalchemy` of `bootstrap`) die je nodig hebt om bepaalde functies te implementeren. Voeg de namen toe en als het onderdeel niet erg standaard is, voeg dan een link naar de website toe. Geef aan welk onderdeel je nodig hebt en waarvoor.

- Voeg een overzicht toe van **vergelijkbare** web-apps of data-pipelines of applicaties, in termen van functies en technische aspecten: wat doen ze? hoe hebben ze het geïmplementeerd? kun je het op dezelfde manier doen? (Besteed een paar regels per "concurrent".)

- Identificeer de **moeilijkste delen** van het implementeren van uw applicatie: denk aan technische problemen of beperkingen die tijdens de ontwikkeling kunnen ontstaan ​​en welke mogelijkheden je hebt om deze te verhelpen.

## Check

Vergelijk voordat je verder gaat je oplossing nog een laatste keer met de projectvereisten. Is het ook nog steeds duidelijk dat je voorgestelde project inderdaad een oplossing is voor het genoemde probleem?

Het projectvoorstel moet goed geschreven en duidelijk opgemaakt zijn. Vergeet niet om een
titel, je naam, en een korte samenvatting van je voorstel op te nemen.

Zorg er ten slotte voor dat je document op spelling is gecontroleerd en dat afbeeldingen **niet te groot** of te klein zijn.


<!--

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

-->
