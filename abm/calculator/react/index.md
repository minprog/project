## React Calculator

Re-create the single page web application of a calculator, but this time while using React.


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
* All React code should be in seperate `.jsx` files.
* CSS code can be included in `.jsx` files or seperate `.css` files.
* The application should be written in React. No other frameworks or extensions are allowed, this includes `JQuery`.
* The application should run on any modern web browser such as Chrome and Firefox. No need to worry about browsers of old such as Internet Explorer.

## Steps

### Create a React app

In this course we will use [Create React App](https://create-react-app.dev/). This is a set of tools pre-configured for developing single page React apps. It allows us to hit the ground running. Go ahead and visit [this get started page](https://create-react-app.dev/docs/getting-started) to get started with a React app.

You might need to install `npm` (Node Package Manager) first. To do this follow [these instructions for WSL under Windows](https://docs.microsoft.com/en-us/windows/dev-environment/javascript/nodejs-on-wsl) or simply execute `brew install node` on Mac OS.

### Digit button

Start by creating a React component for a digit button. Let's call it say, `DigitButton`. Style it in much the same way as your previous Calculator application. Then give it some placeholder functionality such as have it `alert` or `console.log` the number on the button each time the button is pressed.

### Keypad

Create a new component that will house all the buttons of the calculator, a keypad of sorts. Have this component create a button for each of the 10 digits. Place these buttons in much the same way as your previous calculator.

### Display

Then go ahead and create a new component for the display. Style it similarly to your previous application.

### Calculator and state

At this point unsurprisingly perhaps, go ahead and create a new component that will house the entire calculator. This component should effectively create a `Display` and a `Keypad`.

Now you can start thinking about interactions between components. Much like the React tutorial in which you created a tic-tac-toe game, some components will need to keep track of state. In this case the likely candidate is the `Calculator` component. That means you will need to find a way to convey which button was pressed from the `DigitButton` to the `Keypad` and then finally to the `Calculator`. Now is the time to do that and to replace the placeholder functionality of the `DigitButton`s. 

### Add the remaining buttons and functionality

Finally go ahead and add components for the remaining calculation buttons such as `+` and `=`.
