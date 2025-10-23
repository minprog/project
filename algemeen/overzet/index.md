# Git-repository overzetten naar je eigen GitHub-repository

Je hebt aan het project gewerkt in een GitHub Classroom-repository, en na de deadline heb je geen schrijf-toegang meer. Je kunt je werk overzetten naar een persoonlijke GitHub-repository door onderstaande stappen te volgen.

## Stap 1: Clone de Classroom-repository (indien nodig)

Als je de repository **nog niet** op je computer hebt:

    git clone https://github.com/CLASSROOM_ORG/assignment-repo.git
    cd assignment-repo

Heb je de repository al lokaal? Navigeer dan naar de map:

    cd pad/naar/jouw/lokale/repo

## Stap 2: Maak een nieuwe GitHub-repository aan

1. Ga naar [https://github.com/new](https://github.com/new)
2. Kies een naam voor je repository (bijv. `opdracht-naam`)
3. Kies of je de repository openbaar of privé wilt maken
4. **Vink niets aan** bij README, `.gitignore` of licentie
5. Klik op **Create repository**

Je komt nu op een pagina met instructies om een bestaande repository te pushen.

## Stap 3: Voeg je nieuwe repository toe als remote

In je lokale clone:

    git remote rename origin classroom-origin
    git remote add origin https://github.com/JOUW_GEBRUIKERSNAAM/JOUW_REPO_NAAM.git


Dit betekent dat de originele repository een nieuwe "naam" krijgt op jouw computer, namelijk `classroom-origin`.

En de naam `origin` wordt gekoppeld aan de nieuw gemaakte repository. Die naam `origin` is de standaard-koppeling voor git, dus omdat we daar een nieuwe repo aan koppelen werkt daarna alles weer normaal.

## Stap 4: Push je code

Push de inhoud naar je persoonlijke GitHub-repository:

    git push -u origin main

Vergeet de `-u` niet deze eerste keer. Als je daarna wijzigingen gaat maken kun je gewoon `git push` gebruiken.

## Optioneel: Verwijder de classroom-remote

Als je de classroom-remote niet meer nodig hebt:

    git remote remove classroom-origin

Je code staat nu in je eigen GitHub-repository.

---

Krijg je foutmeldingen bij het pushen? Controleer dan of je bent ingelogd bij GitHub in je terminal
of Git-client, en of je schrijfrechten hebt op je eigen repository.
