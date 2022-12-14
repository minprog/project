# Cleanup

Je **code** staat al vast, maar je **repository** is nog niet netjes en volledig. Dit ga je vandaag verbeteren. Deze verbeteringen kun je vervolgens committen en pushen naar je repository op GitHub (geen nieuwe code, wel andere dingen).

## Deel 1: code review

> De review wordt meegenomen in de beoordeling van het **code**-deel van je projectcijfer. Je mag je code niet meer aanpassen, maar in de review kun je laten zien dat je het wel beter had kunnen doen als je nog veel meer tijd had (en hoe je dat dan zou moeten doen!).

Doel van de code reviews is niet om je code nog te uit te breiden of zelfs maar te verbeteren, maar om te reflecteren op de kwaliteit van je eigen code. Je krijgt hierbij hulp van een andere student.

1. Kies een partner.

2. Open je project op je computer en zet je review-partner ervoor. Je partner moet door de code navigeren, niet jij!

3. Je partner zal nu (hardop) commentaar geven op de code en jij gaat zorgvuldig luisteren. Als er vragen zijn, beantwoord deze dan. Noteer die vragen: dit kan zijn waar je project beter kan worden gedocumenteerd, of waar je code duidelijker kan zijn!

De reviewer moet speciaal letten op:

- Hoe gemakkelijk het is om de volledige projectcode te begrijpen (begrijp je waar je dingen moet vinden en waarom ze staan waar ze staan?). Denk daarbij hardop na, zodat de programmeur van het project aantekeningen kan maken.

- Stilistische problemen in de code. Zorg ervoor dat je de zwakke plekken aanwijst, waar het rommelig, onduidelijk of onleesbaar wordt.

Het resultaat van de review plaats je in `REVIEW.md`. Naar verwachting zijn dit wel gemiddeld 5 flinke verbeterpunten die je uitgebreid kunt uitwerken, dus waarover je uitlegt wat het probleem is, hoe het beter zou moeten, en geillustreerd met enkele voorbeelden.

Schrijf bovenaan de file de naam van de student die jouw geholpen heeft met de review.

## Deel 2: cleanup

> De "netheid" van je repository wordt meegenomen in de beoordeling van het **repository**-deel van je eindcijfer.

### README.md helemaal bijwerken

Je GitHub-repository zou een volledig `README.md`-bestand moeten bevatten met de naam van de applicatie, een of twee schermafbeeldingen (**verkleind** naar kleine breedte/hoogte zodat het er goed uitziet als je dit op Github bekijkt), een beschrijving van het doel van het project, en je naam. De `README` moet gemakkelijk te lezen zijn en een snel overzicht geven.


### Toevoegen van ASSESSMENT.md

Bekijk de [studiewijzer](/syllabus) om te zien hoe je project beoordeeld zal worden. In `ASSESSMENT.md` moet je een eenvoudige lijst maken van dingen die je niet wilt dat we missen bij het beoordelen! Wijs ons duidelijk op dingen in de code die je bijzonder aanspreken, of beschrijf functionaliteit van de app waar je bijzonder trots op bent. Normaal nemen we al je code en functionaliteit in aanmerking voor de beoordeling, niet alleen wat je hier opsomt, maar we willen de beste delen natuurlijk niet missen!

Kies ook de grootste beslissingen die je tijdens het project hebt genomen (uit je procesboek!) en schrijf daarover: waarom heb je de beslissing genomen, wat was er niet zo handig aan de vorige ontwerpideeën, waarom is de nieuwe oplossing beter (en is het nog steeds beter, nu je project is afgelopen?). Een kleine alinea, zoals deze, per grote beslissing volstaat.


<!--

### Choosing a license for your work

A copyright statement can be either:

- a *public domain* release, which releases your code to the public without any restrictions (you could also use the *unlicense* for this, see below)

- a *copyright notice* which states who actually owns the rights to the materials in the repository (probably only you)

Copyright is automatic in the Netherlands: if you create something, you own the copyright, but you can release your code to the public domain by stating so in (for example) the `README` file.

If you do want to retain copyright, which is common, then you should note the copyright including the current year, followed by "Alle rechten voorbehouden" or "All rights reserved". This clause means that you will not allow copying, modification, distribution etc.

Even if you claim "All rights reserved," you can add a more liberal license to that, allowing some ways of sharing or modification. This is common for open source projects. If you're proud of your code and want other people to share, you might add an open source license. Anyone who finds your project on GitHub can see that you're fine with sharing!

Follow directions at [GitHub help](https://help.github.com/articles/adding-a-license-to-a-repository/) to add a `LICENSE` file and choose a license that you like, unless you retain all rights for yourself.

-->

### Toevoegen van bronvermelding en dankbetuiging

De `README` moet ook bronnen vermelden van code die je niet zelf hebt geschreven, en afbeeldingen en andere materialen die je niet zelf hebt gemaakt, die onderdeel zijn geworden van je project. Zorg ervoor dat duidelijk is op welke delen/code copyright rust van de verschillende makers. (Bijvoorbeeld: "de code in de map contributions/plotly is copyright 2022 by Plotly.com".)

Voor kleine codefragmenten (bijvoorbeeld van Stack Overflow) hoef je de auteurs niet te vermelden in de `README`. In plaats daarvan schrijf je een kleine opmerking bij de code zelf. Je hoeft de docenten ook niet te vermelden. Zij hebben je graag geholpen, maar claimen geen copyright voor hun bijdragen :-)

**Vergeet niet om alle wijzigingen te pushen naar GitHub!**
