## Forest Fire 2: The Model Revisited

In this second week we have been introduced to the central ideas of Object Oriented Programming (OOP). This way of building models is very useful for ABMs, as it gives us a natural way to capture our agents in classes and give them properties (in the form of `attributes`) and actions (in the form of `methods`). 

For our forest fire model we did not need this yet, because each cell is simply described by a state. However, what happens if we want a burning tree to go empty in exactly three time steps? Then our tree cell will need a memory. An easy and intuitive way to do this is to make an `object` for each cell, and give this object an `attribute` that tracks for how long it has been burning. As such, using OOP allows us to give our agents much more complex behaviors!

Therefore, in this exercise we will reimplement the forest fire model, but now do it in an object-oriented way! Because you have just been introduced to OOP, this may still be a bit overwhelming. We therefore advise you to use the example code from the OOP crash course to get an idea of how to start. 

Most of the same rules apply as in the first forest fire model. However, the following changes need to be applied:

* Each cell is now an `object`, where its state is one of its `attributes`. Only a cell can decide what its own state is!

* You can make a separate `class` for the whole system, which you can call `Forest`. Here, you can store all the seperate cell objects. Also, it is good to have a bunch of methods here that do 'system-wide' operations, such as determining neighbors and computing how much of the forest burned down (which you will need for Forest 3!).

* Use `setters` and `getters` methods, make sure objects can only access and change attributes that they are allowed to (so for instance, a burning cell cannot directly change the state of one of its neighbors!).

* Trees now do not 'burn out' (i.e. $2\rightarrow 0$) with a $20\%$ chance, but after exactly $3$ time steps.

You can still make use of the same visualization code!