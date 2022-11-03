## Forest Fire 1: The Model

The first model we will build from the ground up is used to simulate forest fires. Such a model is an example of an *cellular automata*. This means the systems consists of a grid of **cells**, which each have a certain **state**. This state is changed based on the states of a cell's neighbors. Typically, this happens based on a simple updating rule.

Let's make this a bit more concrete. In our model consists of a 2D grid of cells, where each cell has three states: **empty** (state 0), **tree** (state 1) and **burning** (state 2). The evolution of a cell is $1 \rightarrow 2 \rightarrow 0$. (Some versions also have that a tree can grow back in the empty cell, but we will ignore this for now). Given a tree-node, we decide whether it will catch fire based on the following equation:

<!-- ![ff_equation](ff_eq.png) -->

$$ P(1 \rightarrow 2) = \frac{N_{\text{burning neighbors}}}{N_{\text{neighbors}}}. $$

Here, we use a [Moore neighborhood](https://en.wikipedia.org/wiki/Moore_neighborhood) to establish our neighbors. So, more burning neighbors means a higher chance of catching fire yourself. To establish whether $1\rightarrow2$ happens, compute $P(1 \rightarrow 2)$, and then draw a random value between 0 and 1 (for instance using `np.random.rand()`) and see if this value is smaller than $P(1 \rightarrow 2)$. If this is true, set the tree on fire.

Some further rules:

* A tree that catches fire at time $t$ can only start setting other trees on fire at time $t+1$, otherwise the fire would spread way too fast. You should thus find a way to take this into account when updating.

* Once a tree is on fire (state $2$), it has a 20% chance of burning up each time step it is on fire. If it burns up, the cell becomes empty ($2 \rightarrow 0$).

* For the initialization we introduce a density parameter $D$. This takes values between $0$ and $1$, and determines the density of trees at the start. If $D=0.8$, This means $80\%$ of the grid at the start should be filled with trees. You will thus have to find a way to randomly assign values $1$ and $3$ to the initial grid points.

Putting this all together will give us something like this:

![Forest Fire](forest_fire.gif)


### The Implementation

We will implement this model in `python`. 

* Implement functions that initialize the grid (as a 2-dimensional `numpy` array filled with values `0`, `1`, and `2`). 

* Implement functions that update the states of the cells, based on the rules described above.

Start with a small grid to see if everything works well. After this, make a `100x100` grid, as shown above. (Note that this may take a while to compute!)


### The Visualization

We give you some simple code that you can use to produce the animation shown above. You can put [this](https://raw.githubusercontent.com/minprog/project/2022/abm/forest/forest1/visualize.py) file in the folder of your forest fire and import the `visualize` function. This function takes the following arguments:

* `grid_values: (List[np.ndarray])`: a `list` of the grids (`numpy 2d-arrays`) generated during the simulation.

* `showplot (bool, optional)` : show the visualization (default=`True`).

* `saveplot (bool, optional)`: saves the visualization as a `gif` (default=`False`).

* `filename (str, optional)`: filename used to save animation (default=`simulation_animation`).

* `colors (List[str], optional)`, colors used in animation. Length of list must correspond with number of unique values in grid (i.e. the number of unique states) (default=`['black', 'green', 'red']`).

So, in order to visualize you will need to save all the grids over time in one list. A useful function to create new grids may be `copy.deepcopy`. All arguments that have `optional` after their type do not need to be filled in. So if you run the function by only passing it the array of `numpy` arrays, it will simply show you the visualization and not save it. Also note that you will need to install `matplotlib`.

<!-- Je mag zelf bepalen hoe je de visualisatie wil vormgeven, al moet het wel een bewegend resultaat geven (`.gif`, `.mp4`, of een webpagina waar je het op kan runnen) zoals in het voorbeeld hierboven. Hieronder twee suggesties:

- `matplotlib` ondersteunt animaties, en dit is vrij gemakkelijk te implementeren (zoals je in deze [tutorial](https://matplotlib.org/stable/gallery/animation/dynamic_image.html) kan zien). Als je `matplotlib` gebruikt, is het goed om het grid te visualiseren door middel van een heatmap (`imshow`).
- Als een alternatief: `pygame` is een Python library voor 2D spelletjes, maar kan ook gebruikt worden voor 2D animaties. [Hier](https://www.pygame.org/wiki/tutorials) vind je tutorials.

Het is verstandig om eerst alleen een afbeelding te plotten en dit later uit te bouwen naar een animatie. -->
