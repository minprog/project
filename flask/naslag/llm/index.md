# UvA's AI chat API

If you want to use an `llm` in your project you can do so through UvA's AI chat API. With the benefit that you have access to a wide range of models and you do not have to leave credit card details anywhere. Below are our instructions to get everything set up and running.

## Get your API key

In order to use an llm you will need access. In our case that is in the form of an API key. You can request your own API key by sending us an email at <help@mprog.nl>.

## Using `llm` in Python with UvA's AI chat

You can use the `llm` module to directly interact with a model via the command line:

    $ llm prompt "Think of a good first name for persona who represents a 'Dutch colleague'."
    A good first name for a Dutch colleague might be "Sven." It's a name that's commonly 
    used in the Netherlands and other Scandinavian countries, and it has a friendly, 
    approachable feel to it.

You can also use `llm` for an interactive chat:

    $ llm chat
    Chatting with lite-gpt-4o
    Type 'exit' or 'quit' to exit
    Type '!multi' to enter multiple lines, then '!end' to finish
    > 

And last but not least, you can `import llm` in your Python project to use it from your own code.

## Getting started

1. Install `llm` as a package via the [instructions on the LLM website](https://llm.datasette.io/en/stable/index.html).

2. Install your key by running this command and pasting it in:

        llm keys set openai

3. Configure `llm` to not use the normal OpenAI API but instead the one we have provided for this course.

## Configuration

> For the complete documentation see: <https://llm.datasette.io/en/stable/setup.html>

LLM configuration on macOS is in the directory:

    ~/Library/Application\ Support/io.datasette.llm

or on Linux it might be:

    ~/.config/io.datasette.llm

To add a model to LLM you'll need to add it as an [OpenAI compatible model](https://llm.datasette.io/en/stable/other-models.html#openai-compatible-models).

Create the file `extra-openai-models.yaml` and add, for example, this configuration:

    - model_id: lite-gpt-4o
      model_name: gpt4o
      api_base: "https://ai-research-proxy.azurewebsites.net"
      api_key_name: personal

model_id
: the name you will use inside the `llm` tool

model_name
: the name via which the model is exposed on the API (for now use gpt4o)

api_base
: the base URL for the API

api_key_name
: the name of the key that is set in `llm`

After you have done this, you should be able to set the default model for `llm` using this command:

    llm models default lite-gpt-4o

And then you should be able to run `llm` as per the examples above.

## API use

You should be able to `import llm` and it will pick up the same config as in the command-line tool. Refer to the [LLM Python API documentation](https://llm.datasette.io/en/stable/python-api.html) for more.
