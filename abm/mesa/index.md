## Mesa Tutorial

Until now, we have implemented our models from scratch. However, there are a lot of resources available. In python, the most used package for ABMs is `mesa`. This package is very useful, as it can perform a bunch of tasks that we then do not have to program ourselves anymore (and are often much faster than what we would achieve ourselves). Some examples are easily finding the neighbors of an agent, collecting simulation data, and even visualizing!

We will start by completing the first `mesa` [tutorial](https://mesa.readthedocs.io/en/main/tutorials/intro_tutorial.html). Make sure to complete each step, even though it will be mostly 'copy-paste'. Also make sure you get the same results. In the next module, we will extend on this code, so make sure you can fully reproduce the final product of the tutorial!

You are not obligated to use `mesa` in your own project, but this is encouraged! Be aware that using this package has a bit of a learning curve, but can take away a lot of work further down the road. The tutorial only gives a snapshot of the functionalities of `mesa`, but when you use it to build your own model, you will also need to consult its [documentation](https://mesa.readthedocs.io/en/main/apis/api_main.html), which gives a full overview of all functionalities.

The `mesa` website also has an [advanced tutorial](https://mesa.readthedocs.io/en/main/tutorials/adv_tutorial.html) which shows you how their visualizer works. This creates a plot in your web browser, and can be a nice way to create an interactive plot. Whether you want to use this depends on your own preferences, but be aware it exists!

It is stated in the tutorial that you can use `mesa` both in python scripts (`.py`) and in notebooks (`.ipynb`). Here you should write all your code in `.py`-files, as this will also be the required format for your final project.
