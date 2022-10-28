## ModeyModel Experiment: Redistribution

In order to better understand the `mesa` tutorial, and practice experimenting, we will conduct an experiment with our `MoneyModel`. We now introduce three types of agents:

- The *equalizing* agent: this agent chooses a cellmate with a larger chance if he has a small amount of money.

- The *unequalizing* agent: this agent chooses a cellmate with a larger chance if he has a large amount of money.

- The *standard* agent: this is the same agent as in the tutorial. He gives money to agents in his cell with equal chance.

The model is run with one type of agent, so you do not have to make a model with more than one type of agent. We run the simulation 10 times for each of the three agent types. Then, we look what the effect is on the *gini-coefficient*, which you were already computing in the `mesa` tutorial.


### Weighted choice

We want the chance of choosing a cell mate to be *proportional* to his  wealth level, relative to the other cell mates. For the unequalizing agent, we can easily determine this as:

\\[
    P_{unequalizing}(\text{getting chosen}) = \frac{wealth_i + 0.5}{\sum^N_j (wealth_j + 0.5)}
\\]

So, the chance of getting chosen is equal to your share in the total wealth (in the denumerator, we sum over all \\(N\\) agents). We take \\($wealth_i + 0.5\\) because otherwise agents with no wealth will never be chosen again.

    # retrieve the wealth of the neighbors
    wealth_neighbors = [0, 1, 2, 3]

    # add 0.5 to all wealth levels
    augmented_wealth_neighbors = wealth_neighbors + 0.5
                               = [0.5, 1.5, 2.5, 3.5]

    sum_augmented_wealth_neighbors = 8
    chance_chosen = augmented_wealth_neighbors / sum_wealth_neighbors
                  = [1/16, 3/16, 5/16. 7/16]


Note that the chance of getting money increases with the agent's wealth level. Furthermore, the chances add up to one, which is good!

If we want a equalizing agent, we can invert the chances above:

\\[
    P_{equalizing}(\text{getting chosen}) = \frac{1}{P_{unequalizing}(\text{getting chosen})}
\\]

This example illustrates this again:

    chance_chosen_equalize = 1 / chance_chosen_unequalize
                           = 1 / [1/16, 3/16, 5/16. 7/16]
                           = [16, 16/3, 16/5, 16/7]

Hier zijn de waarden opgeteld niet langer gelijk aan $1$, maar dit is geen probleem. Als je bij `random.choice()` weights gebruikt kijkt de functie alleen naar de relatieve verhoudingen tussen de weights, niet naar de absolute kans. (Je kan de kansen wel *normaliseren* (alle waarden delen door de som van de waarden), waardoor alle waarden opgeteld weer één zijn. Hierdoor krijg je weer de echte kansen te zien.)


### Requirements

Adapt the model from the tutorial such that you can do the following:

- Agents can have a preference for richer (unequalizing) and poorer (equalizing) cellmates.

- You can run the simulation for the three different types of agents, and compute the average gini-coefficient for a given number of runs. You gather your data using the `mesa` data collector.

- You can plot a bar chart with the resulting gini-coefficients. This should look something like this (can you think of a way to plot that also shows the variability?):

![barchart_redist](gini_bars_redist.png)


Run the model with the following parameters:

- Each model has 100 agents
- You run each configuration of the model (at least) 10 times.
- Each simulation has at least 100 time steps.
- The `width` and `height` of the model remain `10x10`.