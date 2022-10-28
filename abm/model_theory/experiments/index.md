## Model Theory 2: Experiments

We do not just build models for fun, but we use them to better understand how the world works. This is especially relevant for systems where physical experiments are very expensive, morally questionable or even impossible. Then, models are basically our only way to perform experiments. 

The nice thing about this is that you, as the modeler, have a lot of freedom! You can just change a parameter value in your model and see how it is affected. Furthermore, you can just add any element to your model you desire. It seems we are only bounded by the computational power of our computer, and our imagination!

This freedom does come with its own problems. Primarily, we now have to think which experiments adequately answer our questions. Furthermore, we need to design experiments that suit our model. If our model does not contain the required mechanism to perform our experiment, it obviously will not work.

Some other important things to remember when running experiments:

* Our models are *stochastic*, meaning each run will be (slightly) different. We will thus have to run our model many times, and aggregate the results before we can draw conclusions.

* Because our models can get quite big, and we have to run them many times, it is likely our simulations will take quite a bit of time. This is why you should *always* save your simulation data. It would be a waste if you are waiting a long time for your data, and some bug in your plotting code throws all your results away! The easiest way is to save your simulation data to a `csv`-file after each simulation.

* The raw data we produce is not very insightful. That is why we always want to plot our data in a clear way. This means we do not just want to show mean values, but also want to give insight into the variability of our data. Here, you can think of plotting with standard deviations or confidence bounds. Also, never forget to label your axes. In `python`, the plotting package `matplotlib` is most-often used, but a nice alternative is `plotly`.


This may all still sound a bit abstract for you, so we in the coming exercises we will put this into practice!