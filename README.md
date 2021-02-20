# IITR chatbot with RASA

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Framework: RASA](https://img.shields.io/badge/Framework-RASA-purple.svg)](https://rasa.com/)

## Overview
The Pandemic has highlighted the significance of online services / tech support- many organizations haven been seen incorporating chatbots for their websites. Seeing this, our project has been proposed in order to develop an assistance Chat Bot for the IIT Roorkee(our institute) website.

## Tech Stack

**ChatBot Framework**
- We have used the **RASA** framework to implement the shell version for our chatbot.
- RASA allows easy integration between the ML and the deployment parts, along with providing a neat architecture for managing the code modules.

**Backend**
- For developing the API for our chatbot, we have used the **Django** framework. It is very light and easily integrable with RASA. This API can then be easily integrated with the IITR website.
- We carried out Web Scraping methods using Beautiful Soup (the python library) to get the URL links of required sections from the institute website.


## Features:
- **For v1**, the ChatBot has been trained while focusing on the following sections:
   - admissions
   - academics, departments, programmes
   - administration
   - research and development
   - awards and scholarships
   - RTI
   - recruitments
   - donations 
   - alumni 
   
 - As proposed, the ChatBot answers humanely, and provides an appropriate answer along with a custom link for specific questions.
 - ![alt hey](https://github.com/mdg-iitr/IITR_ChatBot/blob/master/images/convo.png?raw=true)
 - **Wanna try out the ChatBot yourself? Simply follow the setup instructions below ;)**

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
$ git clone https://github.com/mdg-iitr/IITR_ChatBot.git

```
- Carry out the **second** of the following steps as a solution to this [issue](https://github.com/RasaHQ/rasa/issues/6806):

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
