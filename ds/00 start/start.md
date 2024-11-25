# Data Science

Je hebt vast wel eens gehoord over onderwerpen als (Big) Data Analytics, Machine Learning of Artificial Intelligence. Data Science is namelijk overal om ons heen, van het weerbericht tot Netflix-aanbevelingen. Tijdens de Data Science track ga je ontdekken hoe data inzichten kan creëren en hoe jij deze vaardigheden in de praktijk kunt brengen

## Wat is Data Science?

Data Science draait om het creëren van waarde uit data. Dit wordt veelal gedaan door het toepassen van wiskundige modellen op data. Dat klinkt misschien wat... wiskundig. Maar vrees niet. Je zult erachter komen dat je met een goede dosis programmeerkennis en relatief eenvoudige modellen al een heel eind kan komen. Deze modellen kunnen vervolgens gebruikt worden om (onderzoeks-) vragen te beantwoorden of om voorspellingen te maken. En dat is precies wat je gaat doen tijdens je eigen project!

## Eigen project

Voor je eigen project ben je vrij om zelf een onderwerp en dataset te kiezen. Een Data Science project kan over het algemeen worden opgedeeld in drie belangrijke onderdelen: **Data Processing & Feature Engineering**, **Machine Learning**, en **Data Visualisatie**. Hoewel de meeste projecten elementen van alle drie zullen bevatten, ga jij binnen je project de focus leggen op één van deze pijlers.

We begeleiden je bij elke stap, van het vinden van data tot het ontwikkelen van je projectplan. Dat lijkt moeilijk, maar geen zorgen! Er zijn echt genoeg openbare databases te vinden die zonder al teveel moeite te gebruiken zijn. Hier kun je zelf via verschillende sites naar zoeken, maar kijk sowieso even op [Kaggle](https://www.kaggle.com/) of [deze community-post](https://www.kaggle.com/discussions/general/268890) voor inspiratie. Ook hier 3 projecten die ik zelf (Rayen) heb gemaakt ([1, ](https://www.kaggle.com/code/wenzhuohuruby/signal-13-groupversion)[2, ](https://www.kaggle.com/code/rayenoaf/main-reviews-16)[3](https://www.kaggle.com/code/inescuelifernandez/emo-group-8)); deze zijn niet representatief voor jou eigen project, maar geven hopelijk wel inspiratie.

### **De drie pijlers van Data Science**  

Hier volgt een korte uitleg van de pijlers en wat je ermee kunt doen:  

#### **1. Data Processing & Feature Engineering**  
Data komt in veel vormen en maten. Soms is data netjes en direct bruikbaar, maar vaak is het rommelig, onvolledig of moeilijk te interpreteren. Denk aan datasets met ontbrekende waarden, tekstdata uit tweets of sensorgegevens van apparaten. Het proces van **data processing** draait om het opschonen en voorbereiden van data zodat het bruikbaar wordt. Dit klinkt misschien heel makkelijk of voor de hand liggend, maar kan nog best ingewikkeld zijn.

Daarnaast kun je met **feature engineering** extra informatie uit data halen, bijvoorbeeld door nieuwe kenmerken te creëren die een machine learning-model kunnen helpen. Hoe ingewikkeld en diepgaand dit is hangt heel erg af van het type data.

- **Focus**: Bij deze pijler ligt de nadruk op hoe je een specifiek soort (moeilijke) data voorbereidt en verwerkt voor verdere analyse of voorspellingen.

- **Voorbeelden**:  
   - [Type Data](/ds/resources/install/data_types.md)
   - **Sentimentanalyse van tweets**
      - *Data*: Een dataset met tweets over een specifiek onderwerp (bijv. klimaatverandering of sportevenementen).
      - *Wat te doen*: Verwijder ruis (zoals hashtags, mentions), analyseer veelvoorkomende woorden, maak sentimentlabels (positief, neutraal, negatief), importeer *lexicons*, etc.

   - **Energieverbruik van huishoudens**
      - *Data*: Sensorgegevens van slimme meters in huishoudens (bijvoorbeeld het UCI dataset over energieverbruik).
      - *Wat te doen*: Opschonen van gegevens (missende waarden, pieken), nieuwe features creëren zoals piekverbruikstijden gemiddelden per dagdeel of een meer wiskundige features in de Time & Frequency domain extraheren.

   - **Historische weergegevens**
      - *Data*: Ruwe weergegevens van verschillende steden over de afgelopen 50 jaar.
      - *Wat te doen*: Transformeer gegevens naar een bruikbaar formaat, voeg derivaten toe zoals gemiddelde temperatuur per maand, en creëer visualisaties om patronen te ontdekken.
      
#### **2. Machine Learning (ML)**  
Machine Learning is een veelgebruikte techniek binnen Data Science waarmee je patronen uit data kunt herkennen en voorspellingen kunt doen. ML-modellen werken door data te analyseren en wiskundige regels toe te passen zonder dat ze expliciet geprogrammeerd hoeven te worden.  

In jouw project kun je verschillende ML-modellen gebruiken om antwoorden te vinden op onderzoeksvragen of voorspellingen te doen. Denk bijvoorbeeld aan het voorspellen van huizenprijzen of het herkennen van emoties uit foto's.  

- **Focus**: Bij deze pijler richt je je op het begrijpen en toepassen van verschillende machine learning algoritmes. Je leert hoe je een zo passend mogelijk model maakt met behulp van bestaande of nieuwe algoritmen. Je gaat daarbij ook verschillende soorten modellen met elkaar vergelijken om uiteindelijk een model te maken die een zo valide mogelijk antwoord op je onderzoeksvraag kan geven of een model die betrouwbare voorspellingen kan doen.

- **Voorbeelden**

   - [Machine Learning Algoritmes](/ds/resources/install/ML_algorithms.md) 
   - **Voorspellen van huizenprijzen**
      - *Data*: Een dataset met huizengegevens.
      - *Wat te doen*: Gebruik verschillende algoritmes om huizenprijzen te voorspellen op basis van kenmerken zoals locatie, oppervlakte, en bouwjaar.
   
   - **Objectherkenning in afbeeldingen**
      - *Data*: Een dataset met afbeeldingen of een eigen verzamelde dataset van dieren of verkeersborden.
      - *Wat te doen*: Bouw een classificatiemodel dat objecten kan herkennen en labelen.

   - Dingen die je kan uitzoeken:  
      - Welke modellen zijn allemaal relevant voor mijn dataset?
      - Waarom werkt model A beter dan model B op jouw dataset?  
      - Welke parameters zorgen voor een betere voorspelling?
      - Hoe voorkom je overfitting of underfitting?
      - Wat voor technieken kan ik gebruiken om mijn model te verbeteren?

#### **3. Data Visualisatie**
De inzichten die je uit data haalt, kun je niet altijd direct uit ruwe cijfers aflezen. Daarom is visualisatie een essentieel onderdeel van data science. Data visualisatie helpt om complexe informatie op een eenvoudige en begrijpelijke manier te presenteren, bijvoorbeeld met grafieken, kaarten of interactieve dashboards.  

In jouw project kun je visualisaties gebruiken om een onderzoeksvraag te beantwoorden of een dataset te verkennen. Dit maken jouw resultaten niet alleen inzichtelijk voor jezelf, maar ook voor anderen.  

- **Focus**: Bij deze pijler ligt de nadruk op het begrijpelijk maken van een complexe data en het beantwoorden van een onderzoeksvraag. Doe dit door creatief en effectief de data en conclusies te presenteren.

- **Voorbeelden**:  
   - Creeër een rapport (inleiding -> dataverwerking -> conclusie) rondom een door jou uitgekozen onderzoeksvraag.
   - Een interactieve kaart waarop data visueel inzichtelijk wordt gepresenteerd, zoals demografische gegevens per regio of realtime verkeersinformatie
   - Maak een interactief dashboard doormiddel van een [shiny-app](https://shiny.posit.co/py/)
   - Mogelijke onderzoeksvragen:
      - Hoe ziet (wereldwijde) CO2-uitstoot eruit per land?
      - Zijn er geografische patronen in verkiezingsresultaten?
      - Hoe variëren temperaturen wereldwijd over decennia?
---
<br>

>**Tip**: Denk goed na over welk onderdeel het meest aansluit bij jouw interesse en de vaardigheden die je wilt ontwikkelen. <br>
>Wil je bijvoorbeeld leren hoe je met ruwe data omgaat of is er een specifiek soort data wat je (vanuit jouw werkveld) erg interessant lijkt? Kies dan voor **Data Processing**. <br>
>Wil je meer leren over AI algoritmes en modellen leren toepassen? Ga dan voor **Machine Learning**. <br>
>Of wil je vooral inzicht creëren, leren onderzoek doen en  verhalen vertellen met data? Kies dan voor **Data Visualisatie**.  

Welke focus je ook kiest, wij begeleiden je om je project tot een succes te maken!  

## Voorbereiding

Tot die tijd hebben we verschillende programmeeropdrachten en theorievragen klaargezet bekend te raken met het onderwerp. Bij deze opdrachten ga je leren over een paar modellen die toegepast kunnen worden op data en hoe je dat doet in de programmeertaal Python. Voor deze opdrachten is geen voorkennis nodig. Dit kan betekenen dat ze aan de makkelijkere kant zijn voor studenten die al wat meer statistiek vakken gevolgd hebben. Voor deze studenten geldt; probeer jezelf echt uit te dagen voor het project. Kies bijvoorbeeld een onderwerp waar je nog niet veel ervaring mee hebt of een dataset die wat lastiger is om te verwerken. Hierin zullen wij je ook mee begeleiden.

Tot slot, mocht je opmerkingen, vragen of klachten over wat dan ook over het track hebben, deel deze dan vooral met ons! **Feedback wordt ontzettend gewaardeerd**. Voor ons is het de eerste keer dat deze track zo gegeven wordt, dus elke vorm van feedback helpt ons om het de volgede keren te verbeteren.

## Programma

In onderstaand schema is het rooster voor de eerste week te zien.

| Dag                | Module                               |
|--------------------|--------------------------------------|
| Maandag 25/11      | Set-up en algemeen                   |
| Dinsdag 26/11      | Statistiek & statistische modellen   |
| Woensdag 27/11     | Statistiek & statistische modellen   |
| Donderdag 28/11    | Oefendatasets                        |
| Vrijdag 29/11      | Oefendatasets **iedereen aanwezig**  |

Dit is een leidraad van hoe je je tijd het beste kan verdelen de eerste week. In deze week krijgen jullie in een heel hoog tempo de basics van Data Science aangeleerd, dus het zal deze week hard werken worden. Zorg daarom dat je vooral in deze week alle dagen aanwezig bent zodat je optimaal gebruik kan maken van de TA's en je medestudenten. Mocht je ergens in de week voorlopen, ga dan vooral verder met de module van de volgende dag! Mocht je achterlopen omdat je het lastig vindt of om een andere reden, geef het vooral bij de TA's aan! Op vrijdag 29 november zullen we gezamenlijk aan *Yelp deel 2* opdracht beginnen, maar zullen ook de eerste gesprekken gevoerd worden over jullie eigen project. Daarvoor moet iedereen aanwezig zijn.

Na de eerste week kan je gaan beginnen aan jouw eigen project. Gelijk die maandag (2 december) moet het projectvoorstel al worden ingeleverd. Zorg er daarom voor dat je in de eerste week al gaat nadenken over welk project je zou willen maken en welke data je daarvoor nodig hebt. Na het inleveren van je voorstel kan je aan je project gaan beginnen. Tijdens dit proces zul je verschillende versies van je project in moeten leveren. Hier staan ook deadlines voor. Voor meer informatie over hierover kan je op de pagina's van de verschillende milestones vinden.

## Bijdragen

Grote dank aan Wouter Vrielink en Tim Doolan van de Minor AI voor het meedenken aan deze track en mogen gebruiken van verschillende notebooks & opdrachten.
Ook dank aan Mayla voor het creeëren van de oorspronkelijk Data Science track waarop deze editie gebaseerd is.

