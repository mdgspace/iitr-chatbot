# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

map_dept = {"CSE": "https://cse.iitr.ac.in/", "ECE": "https://cse.iitr.ac.in/", "EE": "https://ee.iitr.ac.in/", "Other": "https://www.iitr.ac.in/Main/pages/_en_Departments__en_.html"}

class ActionDepartmentInfo(Action):

    def name(self) -> Text:
        return "action_show_department_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dept = tracker.slots.get("department_name")
        if dept in map_dept.keys():
            output = "Please find more info about the {} department here: {}".format(dept,map_dept.get(dept))
        else:
            output = "Please find more info about the {} department here: {}".format(dept,map_dept.get("Other"))
        dispatcher.utter_message(text=output)

        return []

