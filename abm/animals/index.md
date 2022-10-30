## Animals

The dynamics of the forest fire model look cool, but our trees do not move, so that is still a bit boring. Let us try to make agents that move in a space. With the tools you have learned until now, you can now make rules upon which agents base their decisions and movements. 

For this, we will now make a simulation with more complex agents: animals. You have a choice to either build a predator-prey model, or a boids model (or both if you have time!). We will describe them below.

These next exercises will be more elaborate than the previous ones, and give you an opportunity to practice all the techniques you have learned before. You get more freedom in how you want to implement the exercises, but this also means you will have to figure our by yourself which components your model needs.

Its also good to practice making your own visualization here. You may want to try `matplotlib` animation, or maybe you want to use the `mesa` visualizer.


### Predator-Prey

The predator-prey model is an ecological model where different animal species compete for food, and hunt each other. The agents will look for food, avoid predators and try to mate. You may have already seen an example in the introduction of this track, and there is a lot of information to find on these type of models. 

It is best to start by making one predator and one prey animal, and see if you can get a stable equilibrium where both species can survive (this is harder than it sounds). After this, add more components and make your system more realistic!


### Boids

Until now, our agents moved in a discrete space. This is the case for many ABMs, but sometimes we want to have our agents move in a more realistic continuous space. You can implement this through the [boids-algorithm](http://www.red3d.com/cwr/boids/). This model is used to simulate swarms of birds or schools of fish (in the introduction we showed an example.) Can you manage to reproduce the complex patterns?

Note that implementing this algorithm is quite a bit more challenging than the previous ones. Do not feel discouraged if you do not manage to get this to work!