## Animals

De dynamica van het forest fire model zien er cool uit, maar de bomen bewegen niet, dus dat is nog een beetje saai. Laten we dus proberen de agents te laten bewegen door de ruimte. We kunnen de agents een 'eigen wil' geven die bepaald hoe ze bewegen. Ze kunnen bijvoorbeeld op zoek gaan eten, andere agents of juist proberen weg te blijven van andere agents. Met zulke complexere agenten kunnen we straks ook menselijk gedrag gaan simuleren. Óf het gedrag van dieren, wat we nu eerst gaan doen.

De volgende opdrachten zijn een stuk uitgebreider dan de vorige, en je hoeft ze dus niet (allebei) af te krijgen. Je krijgt ook alle vrijheid om ze te implementeren hoe je wil. Dit betekent ook dat je maar weinig handvatten krijgt. Je zal zelf uit moeten zoeken hoe het model werkt en wat je erin moet stoppen.


### Predator-Prey

In dit model hebben we twee soorten dieren: roofdieren en prooien. Beide dieren proberen te overleven, alleen doen prooien dit door weg te blijven bij roofdieren, en roofdieren juist door prooien te vangen. Beide soorten planten zich ook voort. Vanuit deze basis kan je dit model zo complex maken als je wilt. Je kan de meerdere soorten dieren introduceren, het terrein aanpassen, en zelfs evolutie toepassen. Probeer zelf dit model te implementeren, en probeer het complexer en interessanter te maken. Ga ook op onderzoek uit hoe de model parameters de dynamica in het model aanpassen. Wanneer sterven er dieren uit? Kan je de populaties stabiel krijgen?


### Boids

De modellen tot nu toe waren nog in een discrete ruimte. Dit is het geval voor veel ABM's, en kan ook zeker goed werken voor jullie eigen project. Maar voor veel applicaties is het logischer om in een continue ruimte te simuleren. Om dit te oefenen, kan je het [boids-algoritme](http://www.red3d.com/cwr/boids/) implementeren. Dit model wordt gebruikt om zwermen vogels of scholen vissen te simuleren. Krijg je het voor elkaar om complexe patronen te reproduceren? (Begin in 2D, maar als je van een uitdaging houdt kan je het ook in 3D proberen!).

(Deze opdracht is moeilijker dan de andere opdrachten. Het is dus geen probleem als je hier niet uit komt.)