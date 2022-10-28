## Forest Fire 3: Experiments

Let's conduct our first experiment on our forest fire model. When initializing our model, we have set the density $D$ of our forest to $0.8$. However, we are now interested if our model will behave differently if this density is changed.

So, we will run a simulation to see if the intial density has an effect on the amount of trees that burn down. This means that you will have to implement the following:

* You will need to track what percentage of the trees have burnt down after each simulation.

* You need to write a function that initializes the forest fire model for a particular value of $D$, runs the full simulation and then collects what percentage of the forest burned down.

* You need to write a way to collect and save the data of these simulations.

* You need to plot the resulting experimental data.

For the experiments, start with a range of densities between $0.1$ and $1.0$. You can take a large step size (for instance $0.1$). For each density $D$, you will need to run the similation at least 10 times. Note that this will already require 100 runs of the model! This may take a while, so first start with a smaller amount of simulations when testing your code! 

The plot should show the percentage of burned trees on the y-axis and the density on the x-asix. It should at least show the average percentage of burned trees, but you should also try to show some form of variability (like showing the standard deviation around the mean).

It is best to use the OOP-version of your forest fire model, as this will also be required in the project.

Looking at the plot, what can you conclude? Is there a *critical density* after which you see a substantial change in how the model behaves?

<!-- ABM modellen worden gebouwd om experimenten te doen die je niet in de echte wereld kan doen. Het is bijvoorbeeld niet heel ethisch om een bos in brand te steken en te kijken hoe snel het afbrand. Gelukkig hebben wij onze `forest fire` model. Met het simpele model dat we nu hebben kunnen we al best veel bestuderen:

- Je kan kijken hoe de dichtheid van de bomen invloed heeft op hoe snel (en óf) het bos afbrand. Wat je hier zal zien is dat er een *kritische* dichtheid is waarna het bos altijd afbrand.
- Je kan ook heterogeniteit introduceren door verschillende 'soorten' bomen te introduceren, die een verschillende brandbaarheid hebben. Wat gebeurt er als je de proporties van de verschillende bomen veranderd.
- Nog een ander experiment in het introduceren van 'obstakels'. Denk bijvoorbeeld aan een meer midden in je bos. Hoe beinvloed dit hoe je bos wordt afgebrand.

Je kan hier een van de experimenten hierboven kiezen, maar het is ook goed als je zelf een experiment bedenkt en implementeert. Bedenk welke aanpassingen je aan je code moet doen om het experiment te laten werken, en welke data je wil verzamelen om de resultaten te beoordelen. -->