# LLM in je project

Wil je een large language model (LLM) gebruiken in je eigen project? Dat kan via de AI-proxy van de UvA. Zo heb je toegang tot een model zonder dat je ergens creditcardgegevens hoeft achter te laten. Hieronder staat hoe je alles instelt, met het model Mistral Small 3.2 dat gratis te gebruiken is.

> Wil je een coding agent gebruiken om je project te bouwen? Zie dan [Agents](/algemeen/agents). Op deze pagina gaat het over het gebruiken van een LLM **in** je eigen programma.

## Je API-key

Om een LLM te kunnen gebruiken heb je toegang nodig. Bij ons is dat een API-key. Heb je er nog geen? Vraag er dan een aan door een e-mail te sturen naar <help@mprog.nl>.

> Je API-key is persoonlijk. Deel hem niet en zet hem **nooit** in een GitHub-repository.

## `llm` gebruiken in Python

Met de module `llm` kun je rechtstreeks vanaf de command line met een model praten:

    $ llm prompt "Verzin een goede voornaam voor een persona die een 'Nederlandse collega' voorstelt."
    Een goede voornaam voor een Nederlandse collega is "Sven". Het is een veelvoorkomende
    naam in Nederland en hij klinkt vriendelijk en toegankelijk.

Je kunt `llm` ook gebruiken voor een interactieve chat:

    $ llm chat
    Chatting with uva-mistral-small-3.2
    Type 'exit' or 'quit' to exit
    Type '!multi' to enter multiple lines, then '!end' to finish
    > 

En tot slot kun je `import llm` doen in je Python-project om een model vanuit je eigen code te gebruiken.

## Aan de slag

1. Installeer `llm` met de [instructies op de website van LLM](https://llm.datasette.io/en/stable/index.html), bijvoorbeeld:

        python -m pip install llm

    Gebruik je [uv](https://docs.astral.sh/uv/)? Dan werkt `uv tool install llm` ook.

2. Sla je key op door dit commando uit te voeren en je key te plakken wanneer erom gevraagd wordt:

        llm keys set uva

3. Stel `llm` zo in dat het niet de gewone OpenAI-API gebruikt, maar de API van de UvA. Instructies staan hieronder.

## Configuratie

> De volledige documentatie vind je op: <https://llm.datasette.io/en/stable/setup.html>

Om een model toe te voegen aan `llm` voeg je het toe als [OpenAI-compatibel model](https://llm.datasette.io/en/stable/other-models.html#openai-compatible-models). Daarvoor maak je het bestand `extra-openai-models.yaml` aan in de configuratiemap van `llm`.

Waar die map staat verschilt per systeem. Op een Mac is het:

    ~/Library/Application\ Support/io.datasette.llm

en op Linux is het meestal:

    ~/.config/io.datasette.llm

Weet je niet zeker waar de map staat, of gebruik je Windows? Voer dan dit commando uit. De map waarin het bestand `logs.db` staat is de configuratiemap:

    llm logs path

Zet dit in het bestand `extra-openai-models.yaml`:

    - model_id: uva-mistral-small-3.2
      model_name: mistral-small-3.2
      api_base: "https://llmproxy.uva.nl/v1"
      api_key_name: uva

model_id
: de naam die je gebruikt binnen de `llm`-tool

model_name
: de naam waaronder het model beschikbaar is in de API (gebruik hier `mistral-small-3.2`)

api_base
: de basis-URL van de API

api_key_name
: de naam van de key die je in `llm` hebt opgeslagen (hierboven `uva`)

Daarna kun je het standaardmodel van `llm` instellen met dit commando:

    llm models default uva-mistral-small-3.2

Nu zou je `llm` moeten kunnen gebruiken zoals in de voorbeelden hierboven. Test het bijvoorbeeld met:

    llm prompt "Zeg hallo in één woord."

## Gebruik in Python

Je kunt `import llm` doen en dan wordt dezelfde configuratie gebruikt als in de command-line tool. Zie de [Python API-documentatie van LLM](https://llm.datasette.io/en/stable/python-api.html) voor meer informatie.
