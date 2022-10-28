import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors as c
import matplotlib.animation as animation
from typing import List


def visualize(grid_values:List[np.ndarray], showplot:bool=True, saveplot:bool=False, 
              filename:str='simulation_animation', colors:List[str]=['black', 'green', 'red']):
    """Animates the Cellular automata simulation result.

    Args:
        grid_values (List[np.ndarray]): a list of the grids (numpy 2d-arrays) generated during the simulation
        showplot (bool, optional): show the visualization. Defaults to True.
        saveplot (bool, optional): saves the visualization as a gif. Defaults to False.
        filename (str, optional): filename used to save animation. Defaults to 'simulation_animation'.
        colors (List[str], optional): colors used in animation. Length of list must correspond with number of 
                                      unique values in grid (i.e. the number of unique states). 
                                      Defaults to ['black', 'green', 'red'].
    """

    # Set up figure and colors
    fig = plt.figure(figsize=(8,8))
    cmap = c.ListedColormap(colors)

    # Plot frames
    ims = [[plt.imshow(grid, vmin=0, vmax=len(colors), cmap=cmap, animated=True)] for grid in grid_values]

    plt.axis('off')
    plt.tight_layout()

    ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)
    
    if saveplot:
        ani.save(filename + '.gif', writer=animation.PillowWriter(fps=20))

    if showplot:
        plt.show()