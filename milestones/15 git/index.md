# Git

Om je project te beheren ga je `git` gebruiken. Met deze tool kun je geregeld (minimaal dagelijks) je werk committen (vastleggen) en pushen (doorzetten) naar de website Github.

Hiermee is goed te zien welke voortgang je maakt en aan het eind van het project is er een historie van het project beschikbaar waarmee wordt aangetoond dat je regelmatig en zelfstandig aan je project hebt gewerkt.

1. Maak een account aan op [github.com](https://github.com/) als je dit nog niet gedaan hebt.

2. Ga naar [Github Classroom om een nieuwe repository aan te maken voor jouw project](https://classroom.github.com/a/MSAwEkpO).

3. Stuur hieronder de link naar de pagina van jouw nieuwe repository in, zodat we deze op een rijtje hebben.

    - Dit is **niet** de link die eindigt op `.git` maar de URL van de webpagina die verschijnt als jij je project hebt aangemaakt.

4. Zet je proposal-document in je git-repository.

## Tips

- Zorg dat je in de regel **nooit** bestanden wijzigt via de pagina op github.com. Gebruik `git` op je eigen computer en `push` de wijzigingen naar github.

- `git` heeft een steile leercurve waar je doorheen moet. Het echte leren doe je door `git` te gebruiken. Over tijd gaat het steeds meer in je vingers zitten. Tot die tijd zal het een beetje frustrerend en onwennig aanvoelen, maar dat is normaal!

- Mocht je onverhoopt een "merge conflict" krijgen, dan heb je misschien even hulp nodig. Het is niet aan te raden om allerlei bronnen op internet te gebruiken. Je kunt namelijk niet goed bepalen welk advies geschikt is voor jouw situatie. We hebben best wel eens gehad dat mensen hierdoor werk zijn kwijtgeraakt.

## Git gebruiken

Je hebt eerder een college over `git` gekeken. Zorg dat je de basiscommando's beheerst en gebruik **niet** de integratie van git in Visual Studio Code of een ander grafisch programma. Dit maakt het namelijk juist ingewikkelder zolang je `git` nog niet goed beheerst.

De terminal-commando's die je nodig hebt om git te gebruiken:

- `git clone https://github.com/...` om de aangemaakte repository op jouw computer te krijgen en aan de Github-repository te linken

    - daarna kun je met `cd` naar de directory van je project gaan

- `git status` om te kijken welke bestanden veranderd zijn

- `git add -A` om alle veranderingen klaar te zetten voor een commit

    - of `git add bestandsnaam.py` om één bestand klaar te zetten voor een commit

- `git commit -m "beschrijving van deze commit"` om het werk van de dag vast te leggen

- `git push` om je werk te synchroniseren met Github.com

Om een bestand terug te zetten naar de versie van de vorige commit (dus alle wijzigingen van de dag weggooien) kun je gebruiken. Doe dit heel zorgvuldig want weg is hier echt weg!

- `git checkout -- bestandsnaam.py`

Het is ook mogelijk om dingen die je al hebt gecommit en gepusht ongedaan te maken. Dit is echter niet zo makkelijk als gebruik van de basiscommando's. Vraag hier hulp bij.
