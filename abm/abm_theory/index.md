# Programmeerproject

## Computational Science: Agent-Based Modelling


Tijdens de Agent-Based Modelling (ABM) track van het programmeerproject gaan we een ABM bouwen dat een echt bestaand systeem simuleert. Hierbij gaan we proberen een 'wetenschappelijke' vraag te beantwoorden, maar deze vraag is vooral om voor jezelf een duidelijk doel te stellen. Het voornaamste doel van dit vak is om een leuk project op te bouwen, waarbij je de dynamieken tussen je agenten complexer ziet worden met elk element wat je toevoegt, en je model steeds beter de werkelijkheid representeerd.

Bij deze track zal je voornamelijk leren hoe je met simulaties moet omgaan. Hoe vertaal ik gedrag uit de 'echte wereld' naar code? Hoe zorg je ervoor dat de simulatie niet te lang duurt? Hoe verzamel je data en interpreteer je deze data? Dit kan je allemaal al doen met de tools we in de vorige vakken behandeld hebben. De moeilijkheid zal dus niet zitten in het leren van een nieuwe taal of platform, maar in het omzetten van een abstract model naar code.

## Wat is Agent-Based Modelling?

ABM is een van de vele modellering-paradigma's binnen de Computational Sciences. Het wordt vooral gebruikt voor systemen waarbij er een hoop agenten zijn die interactie met elkaar hebben. Deze interacties zorgen gezamelijk weer voor dynamica die we niet kunnen verklaren door alleen naar het gedrag van individuen te kijken. Op deze manier stelt ABM ons in staat om systemen te begrijpen waar we het gedrag niet kunnen voorspellen door alleen een stel wiskundige vergelijkingen op te lossen (analytisch). Een aantal begrippen die belangrijk zijn om te begrijpen zijn de volgende:

- **Agent**: Een agent kan alles zijn wat zijn eigen 'gedragsregels' heeft. Dit kunnen mensen zijn voor sociale systemen, dieren in ecologische systemen of 'deeltjes' in natuurkundige systemen. Iedere agent bepaalt zijn eigen gedrag op basis van de eigen voorkeuren en de omgeving, die mede wordt bepaald door het gedrag van anderen.
- **Heterogeniteit**: De agenten zijn niet allemaal hetzelfde (dus niet *homogeen*). Systemen in de echte wereld hebben vrijwel altijd deze eigenschap, maar dit maakt een analytische oplossing vaak moeilijk of onmogelijk. In ABM kunnen we deze eigenschap wel toepassen.
- **Non-lineariteit**: de dynamica van een systeem zijn niet simpelweg een optelsom van de acties van individuele agenten. De acties van agenten hebben invloed op de acties van andere agenten. Dit kan er bijvoorbeeld toe leiden dat een systeem opeens heel snel kan veranderen. Neem als voorbeeld een kudde schapen wat rustig in een veld staat. Als er een paar gaan rennen, komt de rest er meestal achteraan. Dit is niet omdat de schapen individueel besluiten om te gaan rennen en dit toevallig op hetzelfde moment is. Het gedrag van een paar schapen kan opeens het gedrag van de hele kudde beïnvloeden. Andere voorbeelden zijn het plotseling ineenstorten van ecosystemen of het crashen van een aandelenmarkt.
- **Stochastisch**: een systeem is stochastisch als de veranderingen of keuzes worden bepaald door een kans (in plaats van *deterministisch*, waar er een vaste 'if-this-then-that'-regel is voor veranderingen). ABM's hebben altijd stochastische elementen. Dit betekent dat agenten soms hun acties bepalen op basis van een trekking uit een kansverdeling. Dit betekent ook dat elke keer dat je de ABM runt de uitkomst anders zal zijn. 

Ter inspiratie zijn hier wat leuke voorbeelden van YouTube. Deze zijn vaak uitgebreider dan wat we van jullie verwachten, maar geven wel een goed beeld wat je allemaal met ABM kan doen:

- [Bosbranden](https://www.youtube.com/watch?v=LuZAR-yaF-A)
- [Epidemiën](https://www.youtube.com/watch?v=7OLpKqTriio&t=197s)
- [Ecosystemen](https://www.youtube.com/watch?v=r_It_X7v-1E&t=238s)
- [Evolutie/Natuurlijke selectie](https://www.youtube.com/watch?v=0ZGbIKd0XrM)
- [Markten](https://www.youtube.com/watch?v=PNtKXWNKGN8&t=420s)
- [Boids](https://www.youtube.com/watch?v=bqtqltqcQhw&t=6s)
- [Mieren!](https://www.youtube.com/watch?v=81GQNPJip2Y)

Een laatste opmerking is dat bij ABM in een wetenschappelijke context nog een stuk meer statistiek en wiskunde komt kijken. Een model bouwen is één ding, maar de echte moeilijkheid zit erin om te laten zien dat het model daadwerkelijk uitlegt hoe de echte wereld werkt. Wij gaan dit expliciet niét doen. Het voornaamste doel is om een leuk en uitgebreid model te bouwen wat interessante dynamica laat zien. Wel kan je een onderzoeksvraag basseren op de *sensitivity analysis*. Hier kijken we hoe de model-parameters het gedrag van het systeem veranderen, hoe 'gevoelig' het systeem is voor deze parameter. Zo kan je bijvoorbeeld kijken hoe de hoeveelheid deuren de doorstroom van een groep mensen in een ruimte veranderd, hoe de rentestand de hoeveelheid crashes veranderd of hoe de hoeveelheid rijstroken een snelweg betere doorstroom geeft.