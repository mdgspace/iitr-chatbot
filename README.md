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

- Install [RASA](https://rasa.com/docs/rasa/)
```
$ pip3 install rasa==2.0.0rc2
```

- Initialize a **rasa** project
```
$ mkdir rasa_bot
$ cd rasa_bot
$ rasa init
```
The CLI will ask you before training an initial chatbot. Enter **y** and press *enter*.

- Talking to your chatbot: Open another terminal window and run the command:
```
$ rasa run actions
```
This will setup a local server for the custom actions to be executed.

```
$ rasa shell 
```

You can run `rasa shell nlu` to see the intent ranking and confidence.

**Happy Chatting!**
