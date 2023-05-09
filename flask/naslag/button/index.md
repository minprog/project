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