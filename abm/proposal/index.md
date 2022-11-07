# Proposal - ABM

We will now write a proposal for the project we will be working on in the coming weeks. This document gives some specific requirements for this proposal than the ones you can find in the [general proposal requirement](https://project.proglab.nl/milestones/proposal). Be sure to read both documents before starting!

Your proposal for the ABM project should contain the following components:

1. **Description of your [model](https://project.proglab.nl/abm/model_theory/models)**: you shortly explain which system you chose to model and which agents will be in the model.

    * Your model should contain **at least 2 types of agents**, but it is good to include more! Note that a smaller amount of agent types does require their behaviors to be _more_ complex! (see the _scope_ requirement in the general grading guideline). Here, by 'different type' we mean that the agents should have distinct behavioral rules. Merely differentiating one agent type using parameter values therefore does not equate to more agent types.

    * Your agents should live on a **space**. This means they should have a position and are able to move around. You can choose whether this space is discrete or continuous. This also means we expect a  **visualization** of the space. This can be very simple, but should be able to show your agent's movements in a clear way. This also makes it easier to test whether you programmed your agents properly!

    * Clearly state how your agents **interact**, and how this creates the **global behavior** of the system. For global behavior, you can think of the share of infected individuals, a population count of a particular species or the price time series your model generates.

2. **Research question**: after you have described the system, you will formulate a research question, that will shape the experiment you will run on your model. 

    * Formulate a research question that you cannot just answer with 'yes' or 'no', but that is also not so open-ended it is hard to answer. Try something like: _"what is the effect of [intended intervention(s)] on [variable(s) of interest]"_.

    * Are you planning to answer a _scientific_ or _optimization_ question? Be explicit!

    * Your research question should be appropriate for the model you defined. Does your model contain all the **required components** to answer it? Does it not contain unnecessary components (remember Occam's Razor)? Describe shortly why you think why your model is adequate to answer the research question.

3. **Experimental setup**: Which [experiments](https://project.proglab.nl/abm/model_theory/experiments) are you planning to conduct to answer your research question?

    * What parameters will you change, what 'shocks' will you introduce or which components will you add? 
    
    * How do the planned experiments answer your research question?

    * How will you show the experimental results to us? You will have to make at least **1 comprehensive figure** of your experimental results, but it is advisable to make a few! Here you can make a small sketch of the graph(s) you plan to make in the end.

    * Shortly describe how you plan to conduct [calibration and sensitivity analysis]() before you start experimenting. Will you try to use real data? Will you use simple sensitivity analysis, or try a more advanced method?

Your eventual project can differ from what you write in your proposal, but it is a good guideline for where the project should go. Also, it gives the TA's an opportunity to give feedback so you can be sure to have a satisfactory project in the end. 

Also, make sure to make a distinction in what you want to contain in your Minimal Viable Product (MVP), and what you would like to add to your MVP if time permits. 

The components above constitute the **"Problem Statement"** in the [general proposal requirement](https://project.proglab.nl/milestones/proposal). For the **"Solution Sketch"**, we consider a sketch of the planned visualization of the model and figure(s) for the experiment. The **"Prerequisites"** can be:
    
* The (data) sources you plan to use to build and calibrate your model (if applicable).
* Packages you plan to use (e.g. `mesa`).
* Some similar models you found (although this is not necessary).
* What you expect to be the **hardest parts** of the implementation.