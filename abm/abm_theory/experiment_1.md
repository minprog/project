## ModeyModel Experiment: Herverdeling

Om de stof uit de eerste `mesa` tutorial nog wat beter te begrijpen, gaan we een eerste experiment uitvoeren met het `MoneyModel` model dat ons gegeven is. We gaan het model aanpassen zodat we experimenten kunnen doen met drie verschillende soorten agenten:

- De *nivellerende* agent: deze agent kiest een cellmate met een grotere kans als deze weinig geld heeft. Deze agent zal dus de ongelijkheid kleiner proberen te maken.
- De *denivellerende* agent: deze agent kiest een cellmate met een grotere kans als deze veel geld heeft. Deze agent zal dus de ongelijkheid groter proberen te maken.
- De standaard agent: deze agent is hetzelfde als in de tutorial, en kiest dus *uniform* random een cellmate (iedere cellmate heeft een gelijke kans).

Het model heeft telkens maar één soort agent, dus je hoeft geen model te maken waar verschillende soorten agenten door elkaar zitten (maar dit mag je wel proberen als je snel klaar bent!). We runnen de simulatie 10 keer voor elk van de drie agenten, en kijken vervolgens wat het effect is van de verschillende agenten in het model op de gini-coefficient (die je model al berekent na de tutorial). Kan je bedenken wat de waarschijnlijke uitkomst gaat zijn?


### Gewogen keuzes

We willen dat de kans dat een cellmate wordt gekozen wordt *proportioneel* is aan zijn relatieve welvaart. Voor de regressieve agent kunnen we dit makkelijk bepalen met de volgende formule:

$\begin{equation}
    P_{denivellerend}(\text{gekozen worden}) = \frac{welvaart_i + 0.5}{\sum^N_j (welvaart_j + 0.5)}
\end{equation}$

Dus: de kans dat je gekozen wordt is gelijk aan jouw aandeel in de totale welvaart (onderin de breuk sommeren we over alle $N$ agenten). Zoals je ziet nemen we $welvaart_i + 0.5$, omdat anders agenten met $0$ welvaart nooit meer gekozen kunnen worden. De bovenstaande formule wordt duidelijker met een voorbeeld:

    # retrieve the wealth of the neighbors
    wealth_neighbors = [0, 1, 2, 3]

    # add 0.5 to all wealth levels
    augmented_wealth_neighbors = wealth_neighbors + 0.5
                               = [0.5, 1.5, 2.5, 3.5]

    sum_wealth_neighbors = 8
    chance_chosen = wealth_neighbors / sum_wealth_neighbors
                  = [1/16, 3/16, 5/16. 7/16]

Twee dingen vallen hier op. Allereerst zie je dat de kansen groter worden naarmate de welvaart meer is, wat precies is wat we willen. Ten tweede zie je ook dat de kansen optellen tot 1, wat ook logisch is. Als we de kans voor de nivellerende agent willen hebben, kunnen we de bovenstaande kansen gebruiken en deze inverteren:

$\begin{equation}
    P_{nivellerend}(\text{gekozen worden}) = \frac{1}{P_{denivellerend}(\text{gekozen worden})}
\end{equation}$

Als we het voorbeeld hierboven gebruiken kunnen we de geïnverteerde kansen als volgt krijgen:

    chance_chosen_equalize = 1 / chance_chosen_unequalize
                           = 1 / [1/16, 3/16, 5/16. 7/16]
                           = [16, 16/3, 16/5, 16/7]

Hier zijn de waarden opgeteld niet langer gelijk aan $1$, maar dit is geen probleem. Als je bij `random.choice()` weights gebruikt kijkt de functie alleen naar de relatieve verhoudingen tussen de weights, niet naar de absolute kans. (Je kan de kansen wel *normaliseren* (alle waarden delen door de som van de waarden), waardoor alle waarden opgeteld weer één zijn. Hierdoor krijg je weer de echte kansen te zien.)


### Requirements

Pas het model dat je uit de tutorial zo aan dat je het volgende kan doen:

- Agents kunnen, naast uniforme random keuze, voorkeur geven aan rijke buren (denivellerend) of armere buren (nivellerend).
- Je kan een simulatie runnen die voor een model met standaard, denivellerende en nivellerende agenten de gemiddelde Gini-coefficient bepaald voor een aantal runs.
- Je kan een bar chart plotten van de resulterende gini-coefficienten. Die moet er ongeveer als volgt uitzien:

<!-- ![barchart_redist](gini_bars_redist.png = 100x) -->
<p align="center">
<img src="gini_bars_redist.png" alt="drawing" width="400"/>
</p>


Run je model met de volgende parameters:
- Elk model heeft 100 agenten.
- Elke configuratie van het model wordt (minstens) 10 keer gerunt (dus voor elk type agent run je 10 keer).
- Elke simulatie heeft minimaal 100 tijdsstappen.
- De `width` en `height` van het model blijven op 10 bij 10.