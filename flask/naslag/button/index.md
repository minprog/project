# Blauwdruk: een dynamische knop

Het web bestaat uit meer dan stilstaande pagina's. Steeds meer zijn er websites en web-apps die de inhoud van een pagina veranderen terwijl je op de pagina bent. Denk bijvoorbeeld aan: een chat app, Google/Apple Maps en interactieve formulieren. 

Veel hiervan is niet mogelijk met enkel HTML & CSS. Om dit wel mogelijk te maken moeten we code kunnen uitvoeren in de browser van de gebruiker zelf. Dat kan met de programmeertaal JavaScript. Een taal ontworpen om te draaien in een browser en te werken met alles wat leeft de in browser. Dat betekent veel bekende bouwstenen zoals functies, variabelen en loops. Maar ook browser en web specifieke eigenschappen zoals events, het manipuleren van elementen op de pagina, het versturen van HTTP requests en asynchrone functies. 

Hieronder vind je een stapsgewijs ontwerp voor het maken van een knop die zijn werk kan doen zonder de pagina te verlaten. Dit ontwerp kan je uitbreiden en aanpassen voor allerlei vormen van dynamische content.

<details markdown="1"><summary markdown="span">JavaScript spoiler</summary>
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
</details>

## Enkel Flask + HTML & CSS

![embed](https://api.eu.kaltura.com/p/120/sp/12000/embedIframeJs/uiconf_id/23449960/partner_id/120?iframeembed=true&playerId=kaltura_player&entry_id=0_m4hzcabg&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[hotspots.plugin]=1&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=0_z4gdq7fk)

[Video Link](https://video.uva.nl/media/Favorite+Button+using+JavaScript+-+HTML+%26+Flask/0_m4hzcabg)

<details markdown="1"><summary markdown="span"><code>Hoe werkt user.favorite_books.remove?</code></summary>
In dit geval is de relatie tussen gebruikers en boeken een Many to Many relatie:

* Een gebruiker kan veel (Many) favoriete boeken hebben.
* Een boek kan voor veel (Many) gebruikers een favoriet zijn.

Voor een many to many relatie is er een aparte tabel nodig om de relatie op te slaan. De relatie hier is een gebruiker en een boek. Dus is er één kolom voor de gebruikers en één kolom voor de boeken: <code>user_id, book_id</code> bijvoorbeeld.

Nou is die extra tabel alleen een manier om de relatie op te slaan, maar niet hoe je er mee wilt werken in code. Het is natuurlijker om na te denken over een gebruiker haar favoriete boeken of over de gebruikers die fan zijn van een boek. Daarom kan je met een ORM zoals SQLAlchemy deze relatie ook zo modelleren. Door aan de modellen van zowel een gebruiker als een boek een <code>relationship mee te geven</code>. De details hiervan vind je op <https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/models/> en <https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html#many-to-many>. Uiteindelijk maakt dit het mogelijk om via een constructie als `user.favorite_books` te werken met alle favoriete boeken van een gebruiker.
</details>


<details markdown="1"><summary markdown="span">Code van het HTML form</summary>
        
        <form action={{url_for("favorite", isbn=book.isbn)}} method="post">
            <button class="favorite-button" type="submit">
            {% if book in user.favorite_books %}
            ❤️
            {% else %}
            ♡
            {% endif %}
            </button>
        </form>

</details>

<details markdown="1"><summary markdown="span">Code van de Flask route</summary>

        @app.route("/favorite/<isbn>", methods=["POST"])
        @login_required
        def favorite(isbn):

            # Grab the current user
            user = User.query.get(session["user_id"])

            # Grab the book
            book = Book.query.get(isbn)

            # Unfavorite if already favorite
            if book in user.favorite_books:
                user.favorite_books.remove(book)
            # Otherwise favorite book
            else:
                user.favorite_books.append(book)
            
            db.session.add(user)
            db.session.commit()

            return redirect(request.referrer)

</details>


## JavaScript in de Console

![embed](https://api.eu.kaltura.com/p/120/sp/12000/embedIframeJs/uiconf_id/23449960/partner_id/120?iframeembed=true&playerId=kaltura_player&entry_id=0_b5fkt86g&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en_US&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[hotspots.plugin]=1&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=0_xmx77w9x)

[Video Link](https://video.uva.nl/media/Favorite+Button+using+JavaScript+-+Console/0_b5fkt86g)

<details markdown="1"><summary markdown="span">DOM & document?</summary>
Document Object Model. Een representatie om een webpagina, een document te representeren met nodes en objecten. Zodat je vervolgens daar tegenaan kan programmeren. Dit is een standaard op zich, die los staat van programmeertalen. Zo kan je zowel met JavaScript als bijvoorbeeld Python werken. Alleen binnen de browser ben je gebonden aan het gebruik van JavaScript.

De eerste node in de DOM is het hele `document`. Dit is in JavaScript een globale variabele. Vervolgens zijn er verschillende manieren om naar volgende nodes te gaan. Je kan bijvoorbeeld via zogenaamde ouder-kind relaties navigeren, bijvoorbeeld `document.children` geeft alle nodes die direct onder `document` vallen. Maar je kan ook hele sprongen maken naar specifieke (klein)kinderen. Bijvoorbeeld `const list = document.querySelector("ul")` geeft het eerste `<ul>` element in het document. Dit idee kunnen we doortrekken, want `list.querySelector("li")` geeft het eerste `<li>` element binnen die eerste `<ul>`. Zo kan je steeds dieper zoeken!

Zie ook: <https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction>
</details>

<details markdown="1"><summary markdown="span">.querySelector()?</summary>
Over de jaren zijn er verschillende manieren geïntroduceerd om iets van de pagina te selecteren. Kijk je naar een Stack Overflow post van zo'n tien jaar geleden, dan zul je wellicht `getElementsByTagName` of `getElementsById` voorbij zien komen. Dit zijn specifieke functies om op een bepaalde manier elementen uit de pagina op te halen. Dat was prima voor simpele gevallen, maar wordt al gauw complex als je bijvoorbeeld combinaties wil selecteren zoals bijvoorbeeld: geef me alle `<p>` elementen met de class `foo`. 

Dus wat je nog veel vaker zult zien op o.a. Stack Overflow is `$(".foo")`. Dat laatste is namelijk een functie van een framework genaamd jQuery. Een library toen zo populair, dat eigenlijk elke JavaScript programmeur er wel mee werkte. De makers van jQuery hadden een goed idee, namelijk we maken een functie die op dezelfde manier elementen van een pagina kan selecteren als dat CSS dat doet. Iedereen op het web kan toch al werken met CSS en zo hoef je niks extra's te leren. Dat werd de functie `$`.

Dit idee was zo populair dat het uiteindelijk werd opgenomen in de JavaScript taal zelf met de naam `querySelector`. Nu hoef je dus niet een extra library te gebruiken en door de gebruiker te laten downloaden, om toch op een bekende manier elementen van een pagina te selecteren.

Dit gebeurt overigens wel vaker: een framework introduceert iets, de wereld went eraan en later komt het in de standaard van de taal terecht. De ironie is dat de functies die jQuery toen zo populair maakten, nu al in de taal gebakken zitten. Waardoor jQuery vaak niet meer nodig is. Onder andere daardoor wordt jQuery steeds minder gebruikt.
</details>

<details markdown="1"><summary markdown="span">.innerHTML & .innerText?</summary>
DOM elementen hebben veel verschillende eigenschappen. Veel heb je er nooit nodig, totdat je ze een keer wel nodig hebt. Maar twee belangrijke om even uit te lichten: `innerHTML` en `innerText`. Stel je voor we hebben de volgende HTML code:

        <button>
            <strong>Submit!</strong>
        </button>

Doen we `const button = document.querySelector("button")`. Dan krijg je:

    `button.innerHTML` geeft `"<strong>Submit!</strong>"`
    `button.innerText` geeft `"Submit!"`

In beide gevallen is het een string en gaat het erom wat er in de knop staat. Alleen de één geeft je alleen de tekst en de ander ook alle HTML tags er binnen. 
</details>