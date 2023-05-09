# Blauwdruk: een dynamische knop

Het web bestaat uit meer dan stilstaande pagina's. Steeds meer zijn er websites en web-apps die de inhoud van een pagina veranderen terwijl je op de pagina bent. Denk bijvoorbeeld aan: een chat app, Google/Apple Maps en interactieve formulieren. 

Veel hiervan is niet mogelijk met enkel HTML & CSS. Om dit wel mogelijk te maken moeten we code kunnen uitvoeren in de browser van de gebruiker zelf. Dat kan met de programmeertaal JavaScript. Een taal ontworpen om te draaien in een browser en te werken met alles wat leeft de in browser. Dat betekent veel bekende bouwstenen zoals functies, variabelen en loops. Maar ook browser en web specifieke eigenschappen zoals events, het manipuleren van elementen op de pagina, het versturen van HTTP requests en asynchrone functies. 

Hieronder vind je een stapsgewijs ontwerp voor het maken van een knop die zijn werk kan doen zonder de pagina te verlaten. Dit ontwerp kan je uitbreiden en aanpassen voor allerlei vormen van dynamische content.

<details markdown="1"><summary markdown="span">JavaScript spoiler</summary>
    <code>
        <script>
            const buttons = document.querySelectorAll(".favorite-button")

            buttons.forEach((button) => {
                button.addEventListener("click", () => {
                    fetch("/api/favorite/" + button.dataset.isbn)
                        .then((response) => response.json())
                        .then((json) => {
                            if (json.is_favorite) {
                                button.innerText = "❤️"
                            }
                            else {
                                button.innerText = "♡"
                            }
                        }).catch((error) => button.innerText = "ERROR!")
                })
            })
        </script>
    </code>
</details>

## Enkel Flask + HTML & CSS
    