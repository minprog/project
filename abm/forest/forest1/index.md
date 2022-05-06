## Forest Fire 1: Het Model

Het eerste model dat jullie van de grond af gaan opbouwen is een model waarmee we bosbranden simuleren. Zo'n model is een voorbeeld van een *cellular automata*. Dit betekent dat ons systeem bestaat uit een grid van cellen die een bepaalde staat hebben. Hun staat wordt veranderd door een stel gedragsregels die kijken naar hun omgeving. Bij ons is het grid een bos met bomen die in brand kunnen vliegen als een van de bomen ernaast in brand staat. Een punt in het grid kan dus drie staten hebben: er staat een boom, er staat een boom en die staat in brand, of er staat niets. Hieronder zie je een voorbeeld hoe dit er ongeveer uit ziet:

<!-- <p align="center">
<img src=forest_fire.gif width="300" height="300" />
</p> -->

![Forest Fire](forest_fire.gif)


### Het Model

Het model bestaat uit een grid met cellen die een boom, brandende boom of lege plek representeren. Elke tijdstap wordt voor elke cel met een boom bepaald of deze in brand zal vliegen. Dit doen we aan de hand van de volgende regel:

\\[ P(\text{in brand vliegen}) = \frac{N_{\text{brandende buren}}}{N_{\text{ buren}}} \\]

De kans dat een boom wordt aangestoken is dus afhankelijk van de hoeveelheid buurbomen die in brand staan. Als de boom in brand staat blijft dit zo voor een aantal tijdstappen. Hierna is de cel waar de boom stond leeg. Als een boom op tijdsstap \\(t\\) in brand vliegt kan hij niet in diezelfde tijdsstap een buurboom aansteken. Dit kan pas op tijdstap \\(t+1\\).

Het model is relatief simpel. Maar als je eenmaal aan het implementeren bent, zul je zien dat er nog best veel parameters zijn die hier niet worden gegeven. Deze moet je dan zelf bepalen. Experimenteer hier mee en kijk wat de beste resultaten geeft. 


### De Implementatie


We gaan dit model in `python` implementeren en vervolgens visualiseren. Voor de implementatie zijn hier een aantal handvatten:

- Laat het grid bestaan uit een hoogte x breedte hoeveelheid cellen. 
- Implementeer elke cel als een object, niet alleen de cellen die een boom zijn. Binnen de cel kan je dan een status bijhouden ('boom', 'brand', 'leeg')
- Implementeer de simulatie zelf in een aparte functie.

### De Visualisatie

Je mag zelf bepalen hoe je de visualisatie wil vormgeven, al moet het wel een bewegend resultaat geven (`.gif`, `.mp4`, of een webpagina waar je het op kan runnen) zoals in het voorbeeld hierboven. Hieronder twee suggesties:

- `matplotlib` ondersteunt animaties, en dit is vrij gemakkelijk te implementeren (zoals je in deze [tutorial](https://matplotlib.org/stable/gallery/animation/dynamic_image.html) kan zien). Als je `matplotlib` gebruikt, is het goed om het grid te visualiseren door middel van een heatmap (`imshow`).
- Als een alternatief: `pygame` is een Python library voor 2D spelletjes, maar kan ook gebruikt worden voor 2D animaties. [Hier](https://www.pygame.org/wiki/tutorials) vind je tutorials.

Het is verstandig om eerst alleen een afbeelding te plotten en dit later uit te bouwen naar een animatie.
