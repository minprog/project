# Opencode met je UvA API-key

In deze instructies zet je [Opencode](https://opencode.ai/) (de desktop-app) op, zodat je het model Qwen 3.6 kunt gebruiken via de UvA-proxy. Er is een versie voor Mac en voor Windows. Lees voor meer achtergrond eerst [de pagina over de agentic coding pilot](/algemeen/agents).

## Wat heb je nodig?

- Een **API-key** van ons. Deze krijg je gedurende het vak via de mail. Heb je hem niet ontvangen? Mail dan naar <help@mprog.nl>.
- Een computer met macOS of Windows.

> **Let op:** je API-key is persoonlijk. Deel hem niet met anderen en zet hem **nooit** in een GitHub-repository. Het configuratiebestand hieronder staat gelukkig buiten je projectmap, dus als je het daar laat staat het goed.

## Stap 1: Installeer Opencode Desktop

1. Ga naar [opencode.ai/download](https://opencode.ai/download).
2. Download de desktop-app voor jouw systeem:
    - **Mac:** kies de versie voor je processor (Apple Silicon voor M1/M2/M3/M4, anders Intel). Open het gedownloade `.dmg`-bestand en sleep Opencode naar je map *Programma's* (Applications).
    - **Windows:** open het gedownloade installatieprogramma (`.exe`) en volg de stappen.
3. Start de app één keer en sluit hem daarna weer af. Zo worden de mappen die we in de volgende stap nodig hebben aangemaakt.

> Bij het eerste openen op een Mac kan er een melding komen dat de app van het internet is gedownload. Kies dan *Open*. Op Windows kan *SmartScreen* waarschuwen; klik dan op *Meer informatie* en daarna op *Toch uitvoeren*.

## Stap 2: Maak het configuratiebestand

Opencode leest zijn instellingen uit een bestand `opencode.json`. Hierin zetten we de UvA-proxy en het model Qwen 3.6. Dit is de inhoud van het bestand (vervang `JOUW-API-KEY` door je eigen key, behoud de aanhalingstekens):

```json
{
  "$schema": "https://opencode.ai/config.json",
  "model": "uva/Qwen3.6",
  "provider": {
    "uva": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "UvA proxy",
      "options": {
        "baseURL": "https://llmproxy.uva.nl/v1",
        "apiKey": "JOUW-API-KEY"
      },
      "models": {
        "Qwen3.6": { "name": "Qwen 3.6 (UvA)" }
      }
    }
  }
}
```

De naam van het model (`Qwen3.6`) moet precies zo geschreven zijn, met hoofdletter Q en een punt.

### Op een Mac

1. Open de app **Terminal** (zoek via Spotlight met `cmd + spatie`).
2. Maak de map aan en open het bestand in een text editor:

    mkdir -p ~/.config/opencode
    touch ~/.config/opencode/opencode.json
    open -e ~/.config/opencode/opencode.json

3. Plak de inhoud van hierboven in het bestand, vul je API-key in en sla op met `cmd + s`.

### Op Windows

1. Open **PowerShell** (zoek in het startmenu).
2. Maak de map aan en open het bestand in een text editor:

    mkdir "$env:USERPROFILE\.config\opencode" -Force
    notepad "$env:USERPROFILE\.config\opencode\opencode.json"

3. Plak de inhoud van hierboven in het bestand, vul je API-key in en sla op met `ctrl + s`.

> Zorg dat het bestand echt `opencode.json` heet en niet `opencode.json.txt`. Controleer dit in Verkenner via *Beeld* → *Weergeven* → *Bestandsnaamextensies*.

## Stap 3: Start Opencode en kies het model

1. Start de Opencode-app (opnieuw) op.
2. Kies als projectmap de map waarin je aan je project werkt (de map met je git-repository).
3. Controleer onderaan het invoerveld welk model is geselecteerd. Er moet **Qwen 3.6 (UvA)** staan. Staat daar iets anders, klik dan op de modelnaam en kies *Qwen 3.6 (UvA)* uit de lijst.
4. Typ een eenvoudige vraag, bijvoorbeeld: *"Leg in twee zinnen uit wat deze repository doet."* Krijg je een antwoord? Dan werkt alles.

> Kies **alleen** Qwen 3.6. Je API-key heeft maar een heel klein budget voor andere modellen, en die zijn dus snel op. Qwen 3.6 is ongelimiteerd en gratis.

## Als het niet werkt

- **Het model staat niet in de lijst:** sluit Opencode helemaal af en start hem opnieuw. Controleer daarna of het bestand op de goede plek staat, of het geldige JSON is (let op komma's, accolades en aanhalingstekens) en of er geen `.txt` achter de bestandsnaam staat.
- **Foutmelding over authenticatie of "401":** je API-key is niet goed overgenomen. Kopieer hem opnieuw uit de mail, zonder spaties ervoor of erachter.
- **Nog steeds vast?** Mail naar <help@mprog.nl> en vertel welk besturingssysteem je gebruikt en wat de foutmelding is.