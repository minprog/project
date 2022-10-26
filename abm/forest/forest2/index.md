## Forest Fire 2: The Model Revisited

In this second week we are introduced to the central ideas of Object Oriented Programming (OOP). This way of building models is very useful for ABMs, as it gives us a natural way to capture our agents in classes and give them properties (in the form of `attributes`) and actions (in the form of `methods`). 

For our forest fire model we did not need this yet, because each cell is simply described by a state. However, what happens if we want a burning tree to go empty in exactly three time steps? Then our tree cell will need a memory. An easy and intuitive way to do this is to make an `object` for each cell, and give this object an `attribute` that tracks for how long it has been burning. As such, using OOP allows us to give our agents much more complex behaviors!

Therefore, in this exercise we will reimplement the forest fire model, but now do it in an object-oriented way! Because you have just been introduced to OOP, this may still be a bit overwhelming. This is why we provide you with [this]() skeleton code, which already contains some of the main components that we will use. Download the code file and put it in the same folder as your original model, then the visualization should work as well!

**Please note** that starting with OOP can be quite challenging! Do not feel bogged down if you do not manage to get this simulation working immediately. In the coming weeks you will encounter it much more, so there will be enough time to get used to it!