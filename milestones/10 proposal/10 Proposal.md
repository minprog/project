# Proposal

We beginnen met een projectvoorstel (proposal). Dit is een document waarin je het functionele ontwerp van het project koppelt aan een probleem uit de echte wereld. Kort gezegd, wat doet je project om iets echts op te lossen. Hieronder vind je precies hoe en wat.

## Het doel

Projecten hebben altijd een risico van falen. Er zijn signalen die een hoog risico op falen aangeven:

- Het project probeert te veel of te weinig te doen.
- Het doel van het project is erg vaag omschreven.
- Het is niet bepaald duidelijk wie het product gebruikt, of zou willen gebruiken.
- Het probleem dat het project probeert op te lossen bestaat niet of is eigenlijk al opgelost.

Over het algemeen zie je, dat hoe duidelijker het idee van wat het project zou moeten zijn ten einde van het vak, hoe groter de kans op succes. Dat gezegd, succes hier is natuurlijk een goed compleet project. Het gaat hier zeker niet om een populair product of een potentieel commercieel succes.

Er zijn stappen die je kan nemen om de kans op een succesvol project flink te verhogen. Veel daarvan zit in de voorbereiding en in het krijgen van feedback van medestudenten en ook van the staff. Neem nu echt even de tijd om aan dit voorstel te werken en praat met anderen terwijl je eraan werkt. Ideeën uitwisselen en feedback vragen helpt enorm.

## Het format

Maak je proposal in Markdown (`.md`). Dit is een klein taaltje om met tekst tekst op te maken. Beetje zoals HyperText Markup Language, maar dan een veel simpelere MarkDOWN language. Het voelt misschien nu een beetje gek, maar straks gaat je project op GitHub leven en daar wordt voornamelijk dit format gebruikt voor documentatie. Plus, het is lekker makkelijk te leren en snel in gebruik. Reden ook waarom de content van deze website ook in Markdown is geschreven ([underneath the hood](https://raw.githubusercontent.com/minprog/project/2022/milestones/10%20proposal/10%20Proposal.md)).

Hier is een goede website om je op gang te helpen: <https://www.markdownguide.org/>. Check ook vooral de Cheat Sheet op <https://www.markdownguide.org/cheat-sheet/>. En om meteen even te proberen, ga naar <https://dillinger.io/>. Dillinger is een online Markdown editor met een goed voorbeeldbestand. Zo zie je meteen hoe en wat.

Voor Markdown kan je gewoon een teksteditor gebruiken. Zeker Visual Studio Code heeft goede integratie ingebakken zitten en daarom raden we deze ook aan. Druk in VSC op ctrl+shift+v of cmd+shift+v en je hebt meteen een preview openstaan. 

## Wat vragen

Beantwoord in je voorstel de voglende vragen met een paar regels tekst. Tenminste, als de vraag relevant is voor jouw specifieke project.

1. Wat is **het probleem** (niet de oplossing) dat jouw project gaat oplossen. Wees duidelijk en specifiek. Een paar abstracte voorbeelden:

    - Dit is een duidelijk beschreven probleem dat een redelijke groep mensen geregeld tegenkomt omdat er geen goed communicatiemiddel is. Dit kan een web-app goed oplossen.
    - Er is een breed gebrek aan kennis over een bepaald onderwerp. Een interactieve visualisatie of verhalende app mist hier.
    - Dit spelconcept bestaat alleen in de echte fysieke wereld. Maar dit is niet bruikbaar in tijden van isolatie, daarom moet dit een web app worden.

2. Wie zijn je verwachte gebruikers? In andere woorden, voor wie bouw je dit project? Bijvoorbeeld:

    - Oudere mensen die over het algemeen onbekend zijn met het onderwerp van het project.
    - "People on the go"
    - Enkel voor powerusers, zij hebben geen uitleg nodig en willen snel werken.
    - De inwoners van Lab42
    - Me, myself, and I

3. In welke setting wordt je project gebruikt? Een paar voorbeelden:

    - Op een groot scherm dat altijd aanstaat waarbij er geen interactie is. Een admin regelt de configuratie op een apart scherm.
    - Voornamelijk op reis, dus waarschijnlijk op een smartphone.
    - Ieder achter zijn eigen laptop of desktop. Er is een redelijk groot scherm en een toetsenbord is ook aanwezig.

4. Wat doet jouw oplossing anders of beter dan bestaande oplossingen? Wat is je niche? Bijvoorbeeld:

    - Deze app is ontwerpen voor een locatie/bedrijf/groep. Het lost de specifieke eisen en problemen dat deze locatie/bedrijf/groep heeft, dat een generieke app niet kan.
    - Deze oplossing focust op een klein deel van een veel groter probleem, waar nog geen goede oplossing voor bestaat.
  
## Schets je oplossing

Schrijf en **schets** je oplossing. Echt waar, **schets**. Dit is misschien wel de belangrijkste stap van dit hele proces. Want zodra je begint met tekenen, ga je ontdekken wat er echt moet gaan bestaan. Er zijn allemaal kleine dingen waar je overheen schiet als je erover schrijft, maar je ziet zodra je het tekent.

Wat je doet hangt een beetje af van het type project:

- Als je een programma maakt dat zich richt op gebruikers, zeg een spel of een web app, schets dan de gebruikerservaring. In andere woorden, de situatie waar de gebruiker zich in bevindt:

    - Voeg schetsen toe voor hoe het afgemaakte project eruit ziet voor de gebruiker. Als er meerdere schermen zijn, schets ze dan individueel.
    - Maak het duidelijk hoe acties en navigatie werken.
    - Voeg concrete voorbeelden van inhoud toe. Dus niet Lorum ipsum overal.

        ![embed](https://www.youtube.com/embed/j0vP77s_bXc)

    - Zorg ervoor dat je schetsen een compleet overzicht geven van je app.

- Als je een tool of een algoritme maakt voorbijvoorbeeld data analyse of voor het doen van een voorspelling, teken dan de componenten van de oplossing uit. Dit hangt natuurlijk sterk af van wat je gaat maken. Bijvoorbeeld in het geval van data processing zou je de verschillende onderdelen van een data processing pipeline kunnen uittekenen.

In alle gevallen:

- Geef een korte samenvatting van jouw oplossing (een paar zinnen) en verbind het probleem dat je probeert op te lossen. "Deze applicatie zal..."

- Neem een minuutje om een goede tool te vinden om foto's van je schetsen te maken. Kijk bijvoorbeeld naar Microsoft Lens. Een rechte en goede kwaliteit foto maakt een wezenlijk verschil. Zorg er in ieder geval voor dat je tekeningen begrijpbaar zijn. Als we niet redelijkerwijs kunnen lezen of begrijpen wat er staat, kan het ervoor zorgen dat je later aan je project kan beginnen. Dit zorgt voor een kleine achterstand die je uiteindelijk weer moet compenseren. Natuurlijk staat het je ook vrij om te schetsen met een computerprogramma, maar over het algemeen raden we papier aan.

- Plaatjes sla je op als aparte bestanden en kan je vervolgens in Markdown linken. Zie <https://www.markdownguide.org/basic-syntax/#images-1>

## Features

1. Maak een lijst van features die moeten of zouden moeten bestaan voor je project. Dat zijn bijvoorbeeld zaken als een login feature/pagine, een "character creation screen", of een visualisatie stap. Bij het maken van deze lijst, probeer zo specifiek mogelijk te zijn en hou features klein. Het is over het algemeen beter om grotere features op te breken in meerdere kleine.

2. Hak nu je lijst in twee. Eén lijst van features die moeten bestaan, anders is je project niet af. Bijvoorbeeld, een meeting app zonder de mogelijkheid om meetings te maken is niet echt een meeting app. Een andere lijst voor features die je zou willen dat bestaan, maar die niet absoluut cruciaal zijn. Denk hier goed over na en probeer zoveel mogelijk features op de tweede lijst te zetten. Als een feature echt nodig is, en dus op de eerste lijst gaat, schrijf dan even kort op waarom.

3. Tot slot, zet de features op de tweede lijst op volgorde van hoe belangrijk ze zijn voor jouw project. Dit gaat je helpen om te prioritizeren later.

Alles wat je hier schrijft is waarschijnlijk nog incompleet. Op basis van feedback van andere of simpelweg door te werken aan je project, zal je features willen toevoegen of veranderen. Maar door dit werk nu te doen, laat het je straks focussen op de belangrijke stukken uit je project. Daarbij geeft het je een beetje overzicht, waardoor je ook makkelijker kleine stukjes kan afbijten even afhankelijk van hoeveel tijd je hebt die dag. Gecombineerd zorgt dit ervoor dat je aan het einde van het vak niet met een hele mooie app zit voor veilingen, zonder de veilingen.

## Requirements

Je project komt ook met vereisten. Dingen die nodig zijn om je project te laten werken. Dat kan bijvoorbeeld een databron zijn, een bepaalde API of een framework. De vraag hier is, denk goed na over wat er nodig is voor jouw project en waar je dat kan vinden. Dat doe je op basis van wat je **nu** weet. Na het indienden van je projectvoorstel, tijdens feedbackgesprekken met andere studenten of met docenten, kunnen er extra dingen naar voren komen. Wat daaruitkomt kan je later aan je voorstel toevoegen.

- Maak een lijst van alle **gegevensbronen** die je gaat gebruiken. Voeg hier links toe naar de downloadpagina of eventuele APIs die je wilt gebruiken. Schrijf op hoe je toegang krijgt. Vaak zal je een account moeten aanmaken, of in sommige gevallen een mailtje moeten sturen.

- Maak een lijst van **externe componenten** (bijvoorbeeld bibiliotheken zoals `sqlalchemy` of `bootstrap`) die je gaat gebruiken om bepaalde functies te implemtenteren. Geef aan welk onderdeel je nodig hebt en waarvoor.

## Wat wordt moeilijk?

Er zit een boel onzekerheid en onbekendheid in een project als dit. De kans is best groot dat iets erg lastig blijkt of juist reuze meevalt. In ieder geval willen we je aanmoedigen nu alvast na te denken over wat vermoedelijk lastig gaat zijn en vervolgens ook wat eventuele uitwegen zijn. Bijvoorbeeld: zou je multiplayerspel desnoods ook singleplayer kunnen? Maak daarom een lijst van punten die je verwacht moelijk te zijn. Tijdens de bespreking gaan we het hier natuurlijk over hebben. 

## Finishing up

* Geef je project een naam en schrijf natuurlijk ook je eigen naam op.
* Run een spellchecker en kijk nog even naar de Markdown preview. 
* Zorg ervoor dat plaatjes niet te groot of te klein zijn in het voorstel.
* Dubbelcheck dat alle gevraagde onderdelen van het voorstel bestaan.
