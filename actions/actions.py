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
            
map_programme = {"UG": "IITR provides UG (including M.Sc.) courses in 17 branches.", 
                "PG": "IITR provides PG (including Ph.D.) courses in 16 departments."}

map_programme_dept = {"UG": "https://www.iitr.ac.in/academics/pages/Undergraduate_Programmes_Including_M_Sc__.html", 
                    "PG": "https://www.iitr.ac.in/admissions/pages/Postgraduate.html",
                    "PHD": "https://www.iitr.ac.in/admissions/pages/Phd.html"}

map_alumni_awards = {"Research Award": "https://alumni.iitr.ac.in/research",
                    "Distinguished Alumni Award": "https://alumni.iitr.ac.in/awards/daa",
                    "Outstanding Service Award": "http://awards.iitr.ac.in/alumni/osa/outstanding-service-awards.php",
                    "Ramkumar Prize": "http://awards.iitr.ac.in/alumni/ramkumar-awards.php",
                    "Khosla National Award": "https://alumni.iitr.ac.in/research/khosla",
                    "HRED River Ganga Rejuvenation Award": "https://alumni.iitr.ac.in/research/river",
                    "HRED Hydro & Renewable Energy Award": "https://alumni.iitr.ac.in/research/hydronew",
                    "O. P. Jain Memorial Structural Design Award": "https://alumni.iitr.ac.in/research/opjain",
                    "A.S. Arya - IITR Disaster Prevention Award": "https://alumni.iitr.ac.in/research/disaster", 
                    "Gopal Ranjan Technology Award": "https://alumni.iitr.ac.in/research/gopal",
                    "Shamsher Prakash Technology Award": "https://alumni.iitr.ac.in/research/shamsher",
                    "Virendra Nath Malti Mital Award": "https://alumni.iitr.ac.in/research/vnmm",
                    "Prof. A. S. Arya Young Earthquake Engineer Award": "https://alumni.iitr.ac.in/research/earthquake",
                    "Mahesh Varma Technology Innovation Award": "https://alumni.iitr.ac.in/research/mahesh",
                    "S. R. Mehra Memorial Award": "https://alumni.iitr.ac.in/research/mehra"}

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

class ActionFaculty(Action):
    
    def name(self) -> Text:
        return "action_faculty"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dept = tracker.slots.get("department_name")
        output = "The information about the faculty in this {} department can be found at the following link: {}".format(dept,dept)
        dispatcher.utter_message(text=output)

        return []

class ActionAdministration(Action):
    
    def name(self) -> Text:
        return "action_administration"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        admin = tracker.slots.get("admin_name")
        output = "\nYou can find information about the {} at this link:{}".format(admin,"https://www.iitr.ac.in/administration/pages/Institute_Central_Administration.html")
        dispatcher.utter_message(text=output)

        return []

class ActionCenter(Action):
    
    def name(self) -> Text:
        return "action_center"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        center = tracker.slots.get("center_name")
        output = "The information about the {} can be found at the following link: {}".format(center,center)
        dispatcher.utter_message(text=output)

        return []

class ActionDonate(Action):

    def name(self) -> Text:
        return "action_donate"

    def run(self, dispatcher: CollectingDispatcher, 
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text,Any]]:
        
        scheme = tracker.slots.get("scheme_name")
        output = "The information about how to donate for the {} can be found at the following link: {} \nDetailed Information about the payment procedure can be found at {}".format(scheme,"https://alumni.iitr.ac.in/donate/donate", "http://awards.iitr.ac.in/donors/info.php")
        dispatcher.utter_message(text=output)
        return []

class ActionAlumniAwards(Action):
    def name(self) -> Text:
        return "action_alumni_awards"

    def run(self, dispatcher: CollectingDispatcher, 
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text,Any]]:

        award = tracker.slots.get("alumni_award_name")
        if award in map_alumni_awards.keys():
            output = "You can get the information about the {} at {}".format(award,map_alumni_awards.get(award))
        else:
            output = "Distinguished Alumni Award: {}\nOutstanding Service Award: {}\nResearch Award: {}\nRamkumar Prize: {}".format(map_alumni_awards.get("Distinguished Alumni Award"),map_alumni_awards.get("Outstanding Service Award"), map_alumni_awards.get("Research Award"), map_alumni_awards.get("Ramkumar Prize"))
        dispatcher.utter_message(text=output)
        return []