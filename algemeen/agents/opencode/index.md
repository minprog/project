## Opencode met je UvA API-key

In deze instructies zet je [Opencode](https://opencode.ai/) (de desktop-app) op, zodat je de modellen Qwen 3.6 en Mistral Small 3.2 kunt gebruiken via de UvA-proxy. Er is een versie voor Mac en voor Windows. Lees voor meer achtergrond eerst [de pagina over de agentic coding pilot](/algemeen/agents).

### Wat heb je nodig?

- Een **API-key** van ons. Deze krijg je gedurende het vak. Heb je deze niet? Mail even naar <help@mprog.nl>.
- Een computer met macOS of Windows.

> **Let op:** je API-key is persoonlijk. Deel hem niet met anderen en zet hem **nooit** in een GitHub-repository. Het configuratiebestand hieronder staat gelukkig buiten je projectmap, dus als je het daar laat staat het goed.

### Stap 1: Installeer Opencode Desktop

1. Ga naar [opencode.ai/download](https://opencode.ai/download).
2. Download de desktop-app voor jouw systeem:
    - **Mac:** kies de versie voor je processor (Apple Silicon voor M1/M2/M3/M4, anders Intel). Open het gedownloade `.dmg`-bestand en sleep Opencode naar je map *Programma's* (Applications).
    - **Windows:** open het gedownloade installatieprogramma (`.exe`) en volg de stappen.

> Bij het eerste openen op een Mac kan er een melding komen dat de app van het internet is gedownload. Kies dan *Open*. Op Windows kan *SmartScreen* waarschuwen; klik dan op *Meer informatie* en daarna op *Toch uitvoeren*.

### Stap 2: Maak het configuratiebestand

Opencode leest zijn instellingen uit een bestand `opencode.json`. Hierin zetten we de UvA-proxy en de modellen Qwen 3.6 en Mistral Small 3.2. Dit is de inhoud van het bestand (vervang `JOUW-API-KEY` door je eigen key, behoud de aanhalingstekens):


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
                    "Qwen3.6": { "name": "Qwen 3.6 (UvA)" },
                    "mistral-small-3.2": { "name": "Mistral Small 3.2 (UvA)" }
                }
            }
        }
    }


De namen van de modellen (`Qwen3.6` en `mistral-small-3.2`) moeten precies zo geschreven zijn: `Qwen3.6` met hoofdletter Q en een punt, `mistral-small-3.2` helemaal in kleine letters.

#### Op een Mac

1. Open de app **Terminal** (zoek via Spotlight met `cmd + spatie`).
2. Maak de map aan en open het bestand in een text editor:

        mkdir -p ~/.config/opencode
        touch ~/.config/opencode/opencode.json
        open -e ~/.config/opencode/opencode.json

3. Plak de inhoud van hierboven in het bestand, vul je API-key in en sla op.

#### Op Windows

1. Open **Git Bash** (zoek in het startmenu).
2. Maak de map aan en open het bestand in een text editor:

        mkdir -p ~/.config/opencode
        touch ~/.config/opencode/opencode.json
        notepad "$(cygpath -w ~/.config/opencode/opencode.json)"

3. Plak de inhoud van hierboven in het bestand, vul je API-key in en sla op.

> Zorg dat het bestand echt `opencode.json` heet en niet `opencode.json.txt`. Controleer dit in Verkenner via *Beeld* → *Weergeven* → *Bestandsnaamextensies*.

### Stap 3: Start Opencode en kies het model

1. Start de Opencode-app (opnieuw) op.
2. Kies als projectmap de map waarin je aan je project werkt (de map met je git-repository).
3. Controleer onderaan het invoerveld welk model is geselecteerd. Er moet **Qwen 3.6 (UvA)** staan. Staat daar iets anders, klik dan op de modelnaam en kies *Qwen 3.6 (UvA)* uit de lijst. Wil je wisselen naar Mistral, kies dan *Mistral Small 3.2 (UvA)*.
4. Typ een eenvoudige vraag, bijvoorbeeld: *"Leg in twee zinnen uit wat deze repository doet."* Krijg je een antwoord? Dan werkt alles.

> Kies **alleen** Qwen 3.6 of Mistral Small 3.2. Je API-key heeft maar een heel klein budget voor andere modellen, en die zijn dus snel op. Deze twee modellen zijn ongelimiteerd en gratis.

Welk model je kiest?

- **Qwen 3.6** is ons advies voor het meeste werk in Opencode: het is gemaakt voor coderen met een agent (bestanden lezen en aanpassen, tests draaien) en het kan veel van je project tegelijk overzien.
- **Mistral Small 3.2** is een kleiner, algemener model. Handig voor korte vragen, uitleg, documentatie of als tweede mening als Qwen vastloopt.

### Als het niet werkt

- **Het model staat niet in de lijst:** sluit Opencode helemaal af en start hem opnieuw. Controleer daarna of het bestand op de goede plek staat, of het geldige JSON is (let op komma's, accolades en aanhalingstekens) en of er geen `.txt` achter de bestandsnaam staat.
- **Foutmelding over authenticatie of "401":** je API-key is niet goed overgenomen. Kopieer hem opnieuw uit de mail, zonder spaties ervoor of erachter.
- **Nog steeds vast?** Mail naar <help@mprog.nl> en vertel welk besturingssysteem je gebruikt en wat de foutmelding is.

## AGENTS.md: geef de agent context over je project

Een agent weet niets over jouw project, behalve wat hij zelf in je bestanden vindt. Met een bestand `AGENTS.md` in de hoofdmap van je repository vertel je hem vooraf wat hij moet weten. Opencode leest dit bestand aan het begin van elke sessie, dus je hoeft niet steeds hetzelfde uit te leggen.

### Aanmaken

Je hebt twee opties:

1. **Laat Opencode het maken.** Typ in het invoerveld `/init` en Opencode bekijkt je project en schrijft een eerste versie van `AGENTS.md`.
2. **Maak het zelf.** Maak in de hoofdmap van je repository (naast je `README.md`) een bestand `AGENTS.md` en schrijf de inhoud zelf.

Lees het bestand daarna altijd door en pas het aan. Het gaat om jouw project, dus jij moet weten wat erin staat en of het klopt.

### Wat zet je erin?

Houd het kort en concreet. Denk aan:

- **Wat het project is:** een of twee zinnen over wat je app doet en welke technieken je gebruikt (bijvoorbeeld Flask, SQLite).
- **Hoe je het draait:** de commando's om de app te starten en te testen.
- **Afspraken over code:** bijvoorbeeld "gebruik Python 3, schrijf docstrings, houd functies klein".
- **Wat de agent niet mag doen:** bijvoorbeeld "pas de database niet aan zonder te vragen" of "installeer geen nieuwe packages zonder te vragen".

Een voorbeeld:

    # Mijn project

    Een webapp in Flask waarmee je boeken bijhoudt. Data staat in SQLite via SQLAlchemy.

    ## Draaien

    - Start de app: `flask run`
    - Voer de tests uit: `pytest`

    ## Afspraken

    - Schrijf Python 3 met docstrings bij elke functie.
    - Houd routes in `app.py` kort en zet logica in aparte functies.
    - Installeer geen nieuwe packages zonder het eerst te vragen.
    - Pas `books.db` nooit rechtstreeks aan.

> Zet **nooit** je API-key of andere geheimen in `AGENTS.md`. Dit bestand hoort in je repository en wordt dus gedeeld.

## Optioneel: afbeeldingen maken en spraak omzetten naar tekst

Naast Qwen 3.6 en Mistral Small 3.2 zijn er nog twee gratis modellen: `default-image` (afbeeldingen maken) en `whisper-large-v3` (spraak naar tekst). Deze werken niet als chat-model in Opencode, maar je kunt ze wel gebruiken met een klein Python-script. Opencode kan deze scripts ook voor je uitvoeren, als je in `AGENTS.md` zegt wat het script doet.

Installeer eerst het pakket `openai` (dit is alleen de module, je gebruikt gewoon de UvA-proxy):

    python -m pip install openai

Gebruik je [uv](https://docs.astral.sh/uv/)? Installeer het pakket met `uv pip install`:

    uv pip install openai

Activeer de omgeving op een Mac met `source .venv/bin/activate` en op Windows (Git Bash) met `source .venv/Scripts/activate`. Daarna kun je de scripts gewoon met `python` draaien, zoals hieronder.

De scripts lezen je API-key uit het bestand `opencode.json` uit stap 2, dus je hoeft hem nergens anders neer te zetten.

### Afbeelding maken

Sla dit op als `image.py`:

    import base64
    import json
    import sys
    from pathlib import Path

    from openai import OpenAI

    config = json.loads((Path.home() / ".config/opencode/opencode.json").read_text(encoding="utf-8-sig"))
    client = OpenAI(
        base_url="https://llmproxy.uva.nl/v1",
        api_key=config["provider"]["uva"]["options"]["apiKey"],
    )

    result = client.images.generate(model="default-image", prompt=sys.argv[1])
    Path("image.png").write_bytes(base64.b64decode(result.data[0].b64_json))
    print("Opgeslagen als image.png")

Gebruik:

    python image.py "een grote beer in de woestijn"

### Spraak omzetten naar tekst

Sla dit op als `transcribe.py`:

    import json
    import sys
    from pathlib import Path

    from openai import OpenAI

    config = json.loads((Path.home() / ".config/opencode/opencode.json").read_text(encoding="utf-8-sig"))
    client = OpenAI(
        base_url="https://llmproxy.uva.nl/v1",
        api_key=config["provider"]["uva"]["options"]["apiKey"],
    )

    with open(sys.argv[1], "rb") as audio:
        result = client.audio.transcriptions.create(model="whisper-large-v3", file=audio)
    print(result.text)

Gebruik (bijvoorbeeld met een `.wav`- of `.mp3`-bestand):

    python transcribe.py opname.wav

> Je kunt deze scripts in je projectmap zetten. Je API-key staat er niet in, want de scripts lezen hem uit `opencode.json`. Je kunt ze dus veilig committen.