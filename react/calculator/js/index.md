## JavaScript Calculator

Create a single page web application for a calculator using only HTML, CSS & JavaScript.

Accept [this GitHub Classroom invite](https://classroom.github.com/a/edM-awM3)

### Minimal functional requirements

* Support for all 10 digits
* Support for decimal numbers through `.`
* Support for `+`, `-`, `x`, and `/`
* A reset button
* A computation (`=`) button
* An output screen

### Optional features

* Viewable history of past calculations
* The ability to re-use old results in new calculations
* Calculcations in octal and binary
* ...

### Technical requirements

* The application should run on a *single* page.
* All JavaScript code should be in seperate `.js` files.
* All CSS code should be in seperate `.css` files.
* The application should be written in vanilla JavaScript. No frameworks or extensions allowed, this includes `JQuery`.
* The application should run on any modern web browser such as Chrome and Firefox. No need to worry about browsers of old such as Internet Explorer.


## Inspiration

The design of the calculator is completely up to you. However, do just take a quick look as to what other calculators look like. Pay special attention as to where buttons are typically located and how each button behaves.  

![](calculator_mac.png)
![](calculator.png)


## Steps

### Create a frame using HTML/CSS

Start by creating a seperate HTML and CSS file. Then go ahead and lay the foundations for the calculator itself. Add and arrange al the buttons you need. And don't forget to add the display of the calculator!

### Add functionality to buttons

Then proceed by adding functionality to each button. To do this, create a seperate `.js` file and do not forget to include that `.js` file in your HTML file. 

Start with the digit buttons. A press of each should add a number to the display. You will likely need [document.querySelector](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector) and to start listening to the [onclick event](https://www.w3schools.com/jsref/event_onclick.asp).

Once the digit buttons are in order, open up an existing calculator and start trying out different buttons. What does each button really do and what do you want it to do? For instance you might have not realized, but pressing an operation such as `+` will clear the display or in other cases append the `+` sign. That is something you will need to program into your calculator.

### Start calculating

A calculator is a stateful machine. It keeps track of past operations (button presses) and future button presses produce different results based on past actions. That means you will need to track of past actions. How you do this is up to you, but you will likely want to introduce some variables that store arrays or strings of sorts that keep track of the calculation as a whole.

Once a calculation needs to be done, because for instance the `=` button is pressed, start calculating. For this one time it is okay to use the [eval function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval) in JavaScript. If you do, do also read "Never use eval()!" header.


## How to Submit

Submit your repository URL below. This should look something like: `https://github.com/minprog-platforms/your_repo_name`.