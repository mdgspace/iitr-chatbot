# IITR chatbot with RASA

## Setup

- Update **pip**
```
$ pip3 install -U pip
```
- Setup the virtual environment
```
$ python3 -m venv ./venv
$ source ./venv/bin/activate
```
- Install [RASA Open Source](https://rasa.com/docs/rasa/)
```
$ pip3 install tensorflow
$ pip3 install rasa==2.0.0rc2
```
- Initialize a **rasa** project
- The CLI will ask you before training an initial chatbot. **Don't train it for now**.
```
$ mkdir rasa_bot
$ cd rasa_bot
$ rasa init
```
- Carry out any **one** of the following steps as a solution to this [issue](https://github.com/RasaHQ/rasa/issues/6806):

    1. **First Method**: Install a public tokenizer

        - Run `locate convert_tokenizer.py` and navigate to that location.
        - Open `convert_tokenizer.py` and replace the existing `TF_HUB_MODULE_URL = (....)` with `TF_HUB_MODULE_URL = ("https://github.com/connorbrinton/polyai-models/releases/download/v1.0/model.tar.gz")` and save it.

    2. **Second Method**: Use another tokenizer

        - Open `config.yml` file in your `rasa_bot` directory and replace `ConveRTTokenizer` with `WhitespaceTokenizer`.
        - Remove the `ConveRTFeaturizer` field.

- Talking to your chatbot: Open another terminal window and run the command:
```
$ rasa train
$ rasa run actions
```
- This will setup a local server for the custom actions to be executed.
```
$ rasa shell 
```
- You can run `rasa shell nlu` to see the intent ranking and confidence.

**Happy Chatting!**
