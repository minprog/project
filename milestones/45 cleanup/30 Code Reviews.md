# Cleanup

Je **code** staat al vast, maar je **repository** is nog niet netjes en volledig. Dit ga je vandaag verbeteren. Deze verbeteringen kun je vervolgens committen en pushen naar je repository op GitHub (geen nieuwe code, wel andere dingen).

## Deel 1: code review

> De review wordt meegenomen in de beoordeling van het **code**-deel van je projectcijfer. Je mag je code niet meer aanpassen, maar in de review kun je laten zien dat je het wel beter had kunnen doen als je nog veel meer tijd had (en hoe je dat dan zou moeten doen!).

Je gaat twee code reviews doen met een andere student. Doel van de code reviews is niet om je code nog te uit te breiden of zelfs maar te verbeteren, maar om te reflecteren op de kwaliteit van je eigen code. Je krijgt hierbij hulp van andere studenten. 

Doe het onderstaande proces **twee keer**:

1. Kies een partner.

2. Open je project op je computer en zet je review-partner ervoor. Je partner moet door de code navigeren, niet jij!

3. Je partner zal nu (hardop) commentaar geven op de code en jij gaat zorgvuldig luisteren. Als er vragen zijn, beantwoord deze dan. Noteer die vragen: dit kan zijn waar je project beter kan worden gedocumenteerd, of waar je code duidelijker kan zijn!

De reviewer moet speciaal letten op:

- Hoe gemakkelijk het is om de volledige projectcode te begrijpen (begrijp je waar je dingen moet vinden en waarom ze staan waar ze staan?). Denk daarbij hardop na, zodat de programmeur van het project aantekeningen kan maken.

- Stilistische problemen in de code. Zorg ervoor dat je de zwakke plekken aanwijst, waar het rommelig, onduidelijk of onleesbaar wordt.

Het resultaat van de review plaats je in een bestand genaamd `REVIEW.md`. Naar verwachting zijn dit wel gemiddeld 5 flinke verbeterpunten die je uitgebreid kunt uitwerken naderhand.

### Uitwerken van `REVIEW.md`

Nadat je beide code reviews hebt gedaan is het taak om de gevonden verbeterpunten uit te werken. Schrijf allereerst bovenaan `REVIEW.md` de file de namen van de twee studenten die jou geholpen hebben met de review. Dan, werk voor ieder verbeterpunt tenminste het volgende uit:

* Wat is het tegengekomen probleem?
* Hoe zou je dit beter kunnen maken?
* Wat voor afweging maak je? Vaak is een keuze voor iets ook een keuze tegen iets anders.
* Illustreer met enkele voorbeelden.

Let bij de punten die je noemt wel op haalbaarheid en let ook op de details. Het mag best veel werk kosten om een verbetering door te zetten, maar het moet wel mogelijk zijn en kloppen.

## Deel 2: cleanup

> De "netheid" van je repository wordt meegenomen in de beoordeling van het **repository**-deel van je eindcijfer.

### README.md helemaal bijwerken naar het nu

In `README.md` stond voorheen het voorstel van het project. Maar, veel daarvan klopt niet meer bij de realiteit. Zo zul je andere keuzes hebben gemaakt, zaken geschrapt of juist toegevoegd hebben. Kortom, het is tijd om dit bestand bij te werken.

Het doel van een README (op GitHub) is om een goed overzicht te geven van een project en mensen (waaronder jezelf) op gang te helpen. Aan jou de taak om deze README dat ook te laten doen. Er is geen vastgelegd format, maar er zijn wel wat punten die sowieso moeten bestaan:

* De naam van de applicatie en natuurlijk jouw naam.
* Een paar schermafbeeldingen (**verkleind** naar kleine breedte/hoogte zodat het er goed uitziet als je dit op Github bekijkt).
* Een beschrijving van het project. Wat het oplost, wat het doet, voor wie het is, etc.
* Instructies voor het installeren / draaiende krijgen van jouw applicatie. Geen zorgen, wij gaan in principe de app niet zelf installeren en draaien bij het nakijken. Deze instructies zijn voornamelijk voor jezelf in de toekomst, mocht je nog eens verder willen of je project laten zien.
* De nodige referenties naar data-bronnen en andere dependencies. Meer hierover staat onderaan deze pagina.

Kijk voor inspiratie ook goed naar andere README's van andere open-source projecten op GitHub. Als belangrijkste tip, neem even de tijd om de README te schrijven. Het is toch het eerste wat mensen zien als ze jouw project bekijken.

### Toevoegen van ASSESSMENT.md

Als we één ding hebben geleerd over de jaren heen is het wel: zoveel verschillende projecten op eigen computers draaiende krijgen als het vak al is afgelopen, is niet te doen. Dat brengt een heel hoop spanning, stress en frustratie met zich mee voor iedereen. Daarom draaien wij de apps niet zelf na het inleveren. Maar enkel door te kijken naar code is het makkelijk om dingen te missen. Daarom is `ASSESSMENT.md` in het leven geroepen.

Bekijk allereerst de [studiewijzer](/syllabus) om te zien hoe je project beoordeeld zal worden. Aan jou de taak om in `ASSESSMENT.md` een eenvoudige lijst te maken van dingen die je niet wilt dat we missen bij het beoordelen. Wijs ons duidelijk op dingen in de code die je bijzonder aanspreken, of beschrijf functionaliteit van de app waar je bijzonder trots op bent. Normaal nemen we al je code en functionaliteit in aanmerking voor de beoordeling, niet alleen wat je hier opsomt, maar we willen de beste delen natuurlijk niet missen.

Kies ook de grootste beslissingen die je tijdens het project hebt genomen en schrijf daarover: 

* Waarom heb je de beslissing genomen?
* Wat was er niet zo handig aan de vorige ontwerpideeën?
* Waarom is de nieuwe oplossing beter (en is het nog steeds beter, nu je project is afgelopen?)

Een kleine alinea per grote beslissing volstaat.

### Toevoegen van bronvermelding en dankbetuiging

De `README` moet ook bronnen vermelden van code die je niet zelf hebt geschreven, en afbeeldingen en andere materialen die je niet zelf hebt gemaakt, die onderdeel zijn geworden van je project. Zorg ervoor dat duidelijk is op welke delen/code copyright rust van de verschillende makers. (Bijvoorbeeld: "de code in de map contributions/plotly is copyright 2022 by Plotly.com".)

Voor kleine codefragmenten (bijvoorbeeld van Stack Overflow) hoef je de auteurs niet te vermelden in de `README`. In plaats daarvan schrijf je een kleine opmerking bij de code zelf. Je hoeft de assistenten en docenten ook niet te vermelden. Zij hebben je graag geholpen, maar claimen geen copyright voor hun bijdragen :-)

**Vergeet niet om alle wijzigingen te pushen naar GitHub!**
