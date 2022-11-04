# Programmeerproject

## Agent-Based Modelling


During the Agend-based modeling (ABM) track, we will build an ABM that will simulate a real-world system. Such models are widely used in academia and industry to understand many 'messy' or 'complex' systems around us. Here, you can think of the spreading of diseases, ecosystems, road intersections, financial markets and many more! The concept of ABM may still sound a little abstract to you, so we will first define some important concepts, and then look at some examples.


## What is Agent-Based Modelling?

ABM is one of the many modeling 'paradigms' in the Computational Sciences. It is used to simulate behavior of systems in which there are a lot of interacting agents. Let's first look at how we define our 'agent':

- **Agent**: An agent can be any 'actor' in a system with its own behavioral rules. This can be a human in a social system, an animal in an ecological system, or a particle in a physical system. Each actor decides its what to do based on its environment, which is (partially) determined by the other agents, and its own preferences.

- **Heterogeneity**: The agents are not all the same (so not *homogeneous*). Most systems in the real world have this trait, but it is often disregarded when modeling these systems. This is because heterogeneity makes it difficult (or impossible) to solve the model *analytically*. This means we cannot solve a bunch of equations to know what the system will do, but we need to run a simulation.

- **Randomness** (or **Stochasticity**): Often, we are not sure about what exact behavior an agent will perform at a given time. However, we may know which behaviors are possible and how likely they are. Therefore, we will introduce randomness by letting our agents base decisions on draws from a probability distribution, of which you will see many examples in the coming exercises. This means every simulation of our model will be different. Therefore, we can no longer base conclusions on one simulation, but have to run many simulations and aggregate the results. We will also learn ways how to do this.


Combining these individual behaviors and interactions gives us the 'global' behavior of the system. We thus use a 'bottom-up' approach to model the global behavior of a system. This is needed because the systems we model are typically ['complex'](https://en.wikipedia.org/wiki/Complex_system). This means we can not know what the global behavior of the system will be by just looking at the individuals. Instead, from their interactions complicated patterns may arise. We call this process ['emergence'](https://en.wikipedia.org/wiki/Emergence), and it is all around us!

- **Non-linearity**: The dynamics of a system are not simply the sum of the actions of individual agents. Instead, systems in ABM's behave in a nonlinear way, which means that a change in inputs in our system typically does not result in a proportional change in output.

- **Tipping points**: non-linearity is closely related to the idea of a tipping point. Here, the state of our system suddenly changes to another state due to some change in its properties. This can happen due to a shock from outside the system, but can also be caused by random noise pushing the system out of balance. Moreover, it is sometimes even caused by the system *itself* pushing towards its *critical point*. Once the system is pushed past its critical point, it is often very hard to get back to the previous state. Among others, we can see tipping points in [climate systems](https://www.nature.com/articles/d41586-019-03595-0) and [ecosystems](https://www.nature.com/articles/s41559-019-0797-2), but also in social systems such as the [macro-economy](https://www.sciencedirect.com/science/article/pii/S0165188914001924?casa_token=dhrXc4LLVZUAAAAA:fEvzIv82t5CuF3oV567rIDR3i9l3YTOb6NoTC4Nv3v6i6tMc4KuEvDIOzvRgGWdsegtzsAiv9bM), [financial markets](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1540-6261.1991.tb04646.x), [neighborhood segregation](https://link.springer.com/article/10.2307/2061333) and even [the collapse of societies](https://journals.sagepub.com/doi/abs/10.1177/095169280201400203?casa_token=MvXUnPrnoBkAAAAA:93ZOz2DBH9-s--XBaUpqSTyA0GhIvaNt4-G2sDqVLYf5lrH4-_A6kJb_Psjxy76qG-2-8FTrSK4dgg)!


## Some examples

For illustration (and inspiration!) you can find some fun examples below of ABM-type models. There are a bit more advanced than what we expect of you, but they give a nice example of what you can do with ABMs:

- [Epidemics](https://www.youtube.com/watch?v=7OLpKqTriio&t=197s)
- [Ecosystems](https://www.youtube.com/watch?v=r_It_X7v-1E&t=238s)
- [Evolution/Natural selection](https://www.youtube.com/watch?v=0ZGbIKd0XrM)
- [Markets](https://www.youtube.com/watch?v=PNtKXWNKGN8&t=420s)
- [Boids](https://www.youtube.com/watch?v=bqtqltqcQhw&t=6s)
- [Ants!](https://www.youtube.com/watch?v=81GQNPJip2Y)


## The Goal of this track

This track aims to teach you the following:
 1. Define your own research question.
 2. Determining which components have to be in your model,and how they  will act.
 3. Program your model from scratch such that it does not run too long and your results are reproducable by others.
 4. Analyze your results and answer your research question.

Unlike other tracks, we thus do not learn to work with a completely new framework, but instead learn more about how you would use programming for analyzing difficult problems. The tools you will need to do this will be introduced to you in the preparatory exercises of the coming 4 weeks. After this, you will define your own project, for which you can take two approaches:

* **Scientific Approach**: You will study and explain the properties of a system you think is interesting. You will study the effects of changing some conditions in your system. For example, think of an ecosystem where you introduce predators, how will this affect the overall animal population?

* **Optimization Approach**: ABMs are also very well suited to optimization problems. For instance, you are in charge of designing a new intersection and need to know which design gives an optimal traffic flow. You can then first implement this as an ABM and test it.

The system you choose can be one that is relevant in your studies, or maybe you want to do something entirely different! The most important thing is that you are curious to learn more about this system. You have a lot of time to think about this, so do not worry if you have no idea yet!