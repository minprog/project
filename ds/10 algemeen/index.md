# Introductie

Voordat we diep de statistiek en machine learning in duiken, moeten we natuurlijk beginnen bij het begin. In deze module gaan we dat doen!

We beginnen met het kijken van 2 (korte) filmpjes, die een aantal basisonderwerpen van Data Science bespreken. Hierover moet je een paar korte vragen beantwoorden en die antwoorden inleveren.

Daarna ga je beginnen met het behalen van je eerste Kaggle certificaat. Als je deze hebt afgerond, download de pdf hiervan en lever deze ook in!

## Wat is een (wiskundig) model?

Wiskundige modellen helpen ons patronen te begrijpen, voorspellingen te maken, en verbanden tussen variabelen te ontdekken. Ze vereenvoudigen complexe data en maken analyses mogelijk die anders niet uitvoerbaar zijn.

Bekijk onderstaande video en beantwoord de vragen.

[![Video](http://img.youtube.com/vi/yQhTtdq_y9M/0.jpg)](http://www.youtube.com/watch?v=yQhTtdq_y9M&list=PL1Jt9Mfqf6egxIC99vcbWeDWTvOVq-7Mf&index=2 "What is a (mathematical) model?")

**Q1**: Wat is een wiskundig (statistisch) model?

**Q2**: Stel we hebben het volgende model: ``Gewicht in kg = 40 + 5.5 * Gegeten pizza’s per week``. Als iemand 5 pizza’s per week eet, wat is dan zijn/haar verwachte gewicht op basis van dit model? Wat zouden nog andere *variabelen* zijn die in dit model zouden passen?

**Q3**: Stel we berekenen het gemiddelde van de cijfers die behaald zijn voor Programmeren 1, is dit gemiddelde dan ook een model? Waarom wel/niet?

## Meetniveaus

Meetniveaus bepalen welke analyses mogelijk zijn. Ze helpen om data correct te interpreteren en passende statistische methoden te kiezen. Fouten in het begrijpen van meetniveaus leiden tot onjuiste conclusies, analyseer de meet-niveaus van je data daarom meteen!

Bekijk onderstaande video en beantwoord de vraag.

[![Video](http://img.youtube.com/vi/eghn__C7JLQ/0.jpg)](http://www.youtube.com/watch?v=eghn__C7JLQ "Understanding Measurement Levels")


**Q4**: Analyseer de onderstaande variabelen en bepaal:<br>
1. Het type (kwantitatief of kwalitatief).<br>
2. De meetschaal (Nominaal, Ordinaal, Interval of Ratio).<br>

Leg je antwoord uit en motiveer je keuze.<br>
- Leeftijd <br>
- Woonplaats <br>
- Veiligheidsgevoelens in een buurt gemeten met een 5-punts schaal (erg veilig - veilig - neutraal - onveilig - erg onveilig).<br>
- Een cijfer gegeven door buurtbewoners over hoe veilig zij het vinden in de buurt (1-10)<br>


**Q5**: Wat is het verschil tussen een interval- en ratio-schaal? Geef een duidelijke definitie van beide schalen en noem één voorbeeld per schaal.  

**Q6**: Hoe beïnvloedt dit verschil de mogelijke analyses of conclusies die we kunnen trekken uit data die met deze schalen wordt gemeten? Geef concrete voorbeelden van analyses die wel of niet mogelijk zijn.  

**Hint**: Let op het **absoluut nulpunt** bij ratio-schalen en hoe dit invloed heeft op berekeningen zoals verhoudingen (bijv. "twee keer zoveel").  

# Pandas

Nu je een klein beetje theoretische achtergrond hebt, is het tijd om het iets praktischer te maken. Hiervoor maak je de Kaggle course over [pandas](https://www.kaggle.com/learn/pandas). Belangrijk om te weten is dat Kaggle, hoewel het er iets anders uit ziet, ook gewoon gebruik maakt van notebooks.

Na het maken van de Kaggle course, beantwoord je onderstaande vragen:

**Q7**: In deel 6 van de course maak je gebruik van de ``wine_reviews`` dataset. Noem van de volgende kolommen/variabelen de juiste meetniveaus (nominaal, ordinaal, interval, ratio):<br>
- ``country``<br>
- ``price``<br>
- ``points``<br>


**Q8**: Stel je wilt een model maken dat ``points`` voorspelt door middel van een wiskundig model. Welke variabelen zou je uitkiezen & hoe zou het model er uit kunnen zien?

*(Optioneel)*: Hoe zou het model eruit zien als er categorische variabelen in zouden zitten? **Hint**: google iets omtrend dummy-variabels.

*(Vergeet niet je Kaggle-Certificaat als pdf in te leveren!)*
