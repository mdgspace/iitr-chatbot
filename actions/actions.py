# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

map_dept = {"CSE": "https://cse.iitr.ac.in/", 
            "ECE": "https://cse.iitr.ac.in/",
            "EE": "https://ee.iitr.ac.in/",
            "Other": "https://www.iitr.ac.in/Main/pages/_en_Departments__en_.html"}
            
map_programme = {"UG": "IITR provides UG courses in 17 branches.", 
                "PG": "IITR provides M.Tech in 16 departments.",
                "PHD": "IITR provides PHD 16 departments."}

map_programme_dept = {"UG": "https://www.iitr.ac.in/academics/pages/Undergraduate_Programmes_Including_M_Sc__.html", 
                    "PG": "https://www.iitr.ac.in/admissions/pages/Postgraduate.html",
                    "PHD": "https://www.iitr.ac.in/admissions/pages/Phd.html"}

class ActionDepartmentInfo(Action):

    def name(self) -> Text:
        return "action_show_department_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dept = tracker.slots.get("department_name")
        if dept in map_dept.keys():
            output = "IITR has a {} department. For more information visit: {}".format(dept,map_dept.get(dept))
        else:
            output = "Please find informations about the departments here: {}".format(map_dept("Other"))
        dispatcher.utter_message(text=output)

        return []

class ActionProgramme(Action):
    
    def name(self) -> Text:
        return "action_programme"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        prg = tracker.slots.get("programme")
        if prg in map_programme.keys():
            output = "{}\nPlease find the various programmes available under {} here: {}.".format(map_programme.get(prg),prg,map_programme_dept.get(prg))
        else:
            output = "Please visit https://www.iitr.ac.in/admissions/pages/Freshers'_Special:_Main_Page.html for more information."
        dispatcher.utter_message(text=output)

        return []

