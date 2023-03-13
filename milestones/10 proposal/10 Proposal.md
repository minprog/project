# Proposal

We start with a project proposal. That is a document that connects the functional design of the project to a real world problem. Essentially, what does it do to address something real. Below are the required aspects of the proposal.

## Purpose of this document

Projects inherently have some risk of failure, and there are certain signs that indicate a high risk:

- The project tries to do too much or too little.
- The goal is very vaguely defined.
- It is unclear who would (want to) use the product.
- The problem the project adresses does not exist or is already solved.

The overarching theme here is, the clearer your vision on what the project should be by course's end, the higher the chance of success. Mind you, success here is a good finished project. By no means does it need to be a popular or commercial success. 

There are steps you can take to greatly increase the chance of success. A lot of it is in preperation and getting feedback from fellow students and the staff. Take the time to work on your proposal, and even while working on it, talk to others about your ideas and ask for feedback!

## Some questions

In your proposal answer the following questions with a few lines of text. That is, if the question is relevant to your specific project.

1. What is **the problem** (not the solution) that the project will solve? Be clear and specific. For example:

- There is a clearly defined problem that a reasonable group of people faces. A web app is a welcome solution here.
- There is a broad lack of knowledge on a certain topic. An interactive visualization on storytelling app is missing here.
- There is a game concept that only exists in physical form. But in days of isolation this is impossible and it needs to be lifted to a web app.

2. Who are your projected users? Essentially, who are you building this project for. For example:

- Elderly people who are generally unfamiliar with the project's topic.
- People on the move.
- Powerusers only, they know the topic inside and out.
- The inhabitants of Lab42.
- Me, myself, and I.

3. What is or are the setting(s) that your application is used in? For example:

- On an always on big screen with no interaction. An admin handles configuration on a separate screen.
- Primarily used on the go, likely on a smaller device like a smart phone.
- On a laptop or desktop with a relatively big screen and keyboard available.

4. What does your solution do different or better? Essentially, what is your niche. For example:

- 

## Schets van een oplossing

Beschrijf de oplossing in enig detail. Je combineert tekstbeschrijvingen met visuele hulpmiddelen zoals schetsen of diagrammen.

We zien twee opties voor de uitwerking:

-   Als je een gebruikersgericht programma maakt met Django of Unity, schets je de "gebruikerservaring": de situatie waarin een gebruiker zich zou kunnen bevinden en waarvan het gebruik van de website of visualisatie deel uitmaakt.

    -   Voeg een **visuele schets** toe van hoe het uiteindelijke product eruit zal zien voor de gebruiker; als je je voorstelt dat de toepassing meerdere schermen heeft, schets deze dan allemaal afzonderlijk. Geef duidelijk de mogelijke gebruikersinteracties aan (klik op de knop, ga naar de volgende pagina) en voeg concrete voorbeelden van inhoud toe.

        ![embed](https://www.youtube.com/embed/j0vP77s_bXc)

     - Je schetsen moeten een compleet overzicht geven van wat je gaat maken.

-   Als je tools en algoritmen maakt om data-analyse of voorspelling uit te voeren met behulp van ABM of Data Science, schets je de verschillende componenten waaruit je oplossing bestaat, misschien de onderdelen waaruit het model zal bestaan of de stappen in de dataverwerking die nodig zijn.

In alle gevallen:

-   Vat je idee in één of twee zinnen samen en verbind het met het probleem dat je hebt gedefinieerd. "Deze toepassing zal..."

-   Gebruik een goed hulpmiddel om je schetsen of diagrammen te fotograferen en deze om te zetten in een afbeelding van goede kwaliteit om in het voorstel in te voegen. Je kunt je schets ook opsplitsen in meerdere delen die je afzonderlijk in het document plaatst. Je kunt ook schetsen met een computerprogramma.

-   Als je schetsen onleesbaar zijn, of je hebt niet rechtop ingevoegd, of er ontbreken duidelijk noodzakelijke schermen, dan wordt je voorstel (nog) niet bekeken. Dit vertraagt je project en dat moet je compenseren. Met andere woorden: neem de tijd om goede diagrammen te tekenen.

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
