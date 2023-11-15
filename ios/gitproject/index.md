# Git

Om je project te beheren ga je `git` gebruiken. Met deze tool kun je geregeld (minimaal dagelijks) je werk committen (vastleggen) en pushen (doorzetten) naar de website Github.

Hiermee is goed te zien welke voortgang je maakt en aan het eind van het project is er een historie van het project beschikbaar waarmee wordt aangetoond dat je regelmatig en zelfstandig aan je project hebt gewerkt.

1. Maak een account aan op [github.com](https://github.com/) als je dit nog niet gedaan hebt.

2. Ga naar [Github Classroom om een nieuwe repository aan te maken voor jouw project](https://classroom.github.com/a/o1QAKrnH).

3. Stuur hier ook de link naar de pagina van jouw nieuwe repository in, zodat we deze op een rijtje hebben.

    - Dit is **niet** de link die eindigt op `.git` maar de URL van de webpagina die verschijnt als jij je project hebt aangemaakt.

4. Zet je proposal-document in je git-repository.

## Tips

- Zorg dat je in de regel **nooit** bestanden wijzigt via de pagina op github.com. Gebruik `git` op je eigen computer en `push` de wijzigingen naar github.

- `git` heeft een steile leercurve waar je doorheen moet. Het echte leren doe je door `git` te gebruiken. Over tijd gaat het steeds meer in je vingers zitten. Tot die tijd zal het een beetje frustrerend en onwennig aanvoelen, maar dat is normaal!

- Mocht je onverhoopt een "merge conflict" krijgen, dan heb je misschien even hulp nodig. Het is niet aan te raden om allerlei bronnen op internet te gebruiken. Je kunt namelijk niet goed bepalen welk advies geschikt is voor jouw situatie. We hebben best wel eens gehad dat mensen hierdoor werk zijn kwijtgeraakt.

## Git gebruiken

Er is een college over `git` beschikbaar. Zorg dat je dit voor begin van het volgende vak kijkt, zodat je de basiscommando's beheerst en weet hoe je `git` ook in je terminal kan gebruiken.

Voor dit project ga je alsnog de git integratie in Xcode gebruiken.

In Xcode onder `Integrate` vind je een aantaal commando's, waaronder de volgenden, die je vaak nodig hebt om git te gebruiken:

- `clone` om de aangemaakte repository op jouw computer te krijgen en aan de Github-repository te linken. Dit is een alternatief voor de procedure omschreven in de [GitHub Set-Up Pagina](/ios/github).

- `stage all changes` om alle veranderingen klaar te zetten voor een commit

    - of `stage changes in selected files` om één bestand klaar te zetten voor een commit

- `commit` hiervoor wil je ook altijd een informatieve korte omschrijving mee te geven, om het werk van de dag vast te leggen en met woorden de verandering duidelijk te maken

- `push` om je werk te synchroniseren met Github.com

Het is ook mogelijk om dingen die je al hebt gecommit en gepusht ongedaan te maken. Dit is echter niet zo makkelijk als gebruik van de basiscommando's. Vraag hier hulp bij.
