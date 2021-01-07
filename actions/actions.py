# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

map_dept = {"CSE": "cse",
            "ECE": "ece", 
            "EE": "electrical", 
            "CE": "civil", 
            "Biotech": "biotechnology", 
            "CH": "chemical", 
            "Arch": "architecture", 
            "ASE": "ase", 
            "Chem": "chemistry", 
            "Earth": "earthquake", 
            "EarthSci": "earth_sciences", 
            "HSS": "humanities", 
            "Hydro": "hydrology", 
            "HRE": "hydro_and_renewable_energy", 
            "Management": "management", 
            "Maths": "mathematics", 
            "MIE": "mechanical", 
            "MME": "metallurgy", 
            "Paper": "paper_technology", 
            "Poly": "polymer", 
            "Physics": "physics", 
            "Water": "water_resource"}

map_center = {"ICC": "ICC",
              "IIC": "institute_instrumentation_center", 
              "TL": "tinkering_lab", 
              "IPRC": "intellectual_property_rights_cell", 
              "WFF": "water_for_welfare", 
              "Hospital": "Hospital", 
              "TIDES": "TIDES", 
              "MGCL": "MGCL", 
              "EC": "e-Learning", 
              "DIC": "design_innovation_center", 
              "CEC": "CEC", 
              "CTRANS": "CTRANS", 
              "CoEDMM": "disaster_mitigation", 
              "COE": "list", 
              "NoidaCentre": "greater_noida_extension", 
              "CoN": "nanotech"}

map_programme = {"UG": "IITR provides UG (including M.Sc.) courses in 17 branches.", 
                "PG": "IITR provides PG (including Ph.D.) courses in 16 departments.",
                "PHD": "IITR provides PG (including Ph.D.) courses in 16 departments."}

map_alumni_awards = {"Research Award": "research_award",
                    "Distinguished Alumni Award": "distinguished_alumni_award",
                    "Outstanding Service Award": "outstanding_service_award",
                    "Ramkumar Prize": "ramkumar_prize",
                    "Khosla National Award": "khosla_national_award",
                    "HRED River Ganga Rejuvenation Award": "HRED_river_ganga_rejuvenation_award",
                    "HRED Hydro & Renewable Energy Award": "HRED_hydro_&_renewable_energy_award",
                    "O. P. Jain Memorial Structural Design Award": "OP_jain_memorial_structural_design_award",
                    "A.S. Arya - IITR Disaster Prevention Award": "AS_arya_IITR_disaster_prevention_award", 
                    "Gopal Ranjan Technology Award": "gopal_ranjan_technology_award",
                    "Shamsher Prakash Technology Award": "shamsher_prakash_technology_award",
                    "Virendra Nath Malti Mital Award": "virendra_nath_malti_mital_award",
                    "Prof. A. S. Arya Young Earthquake Engineer Award": "Prof. A. S. Arya Young Earthquake Engineer Award",
                    "Mahesh Varma Technology Innovation Award": "Mahesh Varma Technology Innovation Award",
                    "S. R. Mehra Memorial Award": "S. R. Mehra Memorial Award"}

class ActionContact(Action):
    
    def name(self) -> Text:
        return "action_contact"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        r = requests.get("http://mdg.iitr.ac.in/projects/iitr_chatbot/api/chatbot/Admission/about_us/contact_info")
        data = r.json()
        output = "Please find the contact information here: {}".format(data["url"])

        dispatcher.utter_message(text=output)

        return []

class ActionDepartmentInfo(Action):

    def name(self) -> Text:
        return "action_show_department_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dept = tracker.slots.get("department_name")
        if dept in map_dept.keys():
            r = requests.get("http://mdg.iitr.ac.in/projects/iitr_chatbot/api/chatbot/Admission/departments/{}".format(map_dept.get(dept)))
            data = r.json() 
            output = "IITR has a {} department. For more information visit: {}".format(dept,data["url"])
        else:
            r = requests.get("http://mdg.iitr.ac.in/projects/iitr_chatbot/api/chatbot/Admission/departments/list")
            data = r.json()
            output = "Please find informations about the departments here: {}".format(data["url"])
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
            r = requests.get("http://mdg.iitr.ac.in/projects/iitr_chatbot/api/chatbot/Admission/departments/{}".format(prg))
            data = r.json()
            output = "{}\nPlease find the various programmes available under {} here: {}.".format(map_programme.get(prg),prg,data["url"])
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
        if dept in map_dept.keys():
            r = requests.get("http://mdg.iitr.ac.in/projects/iitr_chatbot/api/chatbot/Admission/faculty/{}".format(map_dept.get(dept)))
            data = r.json() 
            output = "The information about the faculty in this {} department can be found at the following link: {}".format(dept,data["url"])
        else:
            r = requests.get("http://mdg.iitr.ac.in/projects/iitr_chatbot/api/chatbot/Admission/faculty/list")
            data = r.json()
            output = "Please find informations about the faculties here: {}".format(data["url"])
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
        
        cent = tracker.slots.get("center_name")
        if cent in map_center.keys():
            r = requests.get("http://mdg.iitr.ac.in/projects/iitr_chatbot/api/chatbot/Admission/centers/{}".format(map_dept.get(cent)))
            data = r.json() 
            output = "The information about the {} can be found at the following link: {}".format(cent,data["url"])
        else:
            r = requests.get("http://mdg.iitr.ac.in/projects/iitr_chatbot/api/chatbot/Admission/departments/list")
            data = r.json()
            output = "Please find informations about the centers here: {}".format(data["url"])

        dispatcher.utter_message(text=output)

        return []

class ActionRTI(Action):
    def name(self) -> Text:
        return "action_RTI"

    def run(self, dispatcher: CollectingDispatcher, 
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text,Any]]:
    
        response = requests.get("http://mdg.iitr.ac.in/projects/iitr_chatbot/api/chatbot/Right_To_Information/information/RTI")
        json_data = response.json()
        url = json_data["url"]
    
        output = "You can find more information about RTI process at {}".format(url)
        dispatcher.utter_message(text=output)
        return []

class ActionTopDonors(Action):
    def name(self) -> Text:
        return "action_top_donors"

    def run(self, dispatcher: CollectingDispatcher, 
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text,Any]]:
    
        response = requests.get("http://mdg.iitr.ac.in/projects/iitr_chatbot/api/chatbot/Donations/link_to/donations")
        json_data = response.json()
        url = json_data["url"]
    
        output = "You can get information about the Top Donors at {}".format(url)
        dispatcher.utter_message(text=output)
        return []

class ActionDonationSchemes(Action):
    def name(self) -> Text:
        return "action_alumni_schemes"

    def run(self, dispatcher: CollectingDispatcher, 
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text,Any]]:
    
        response = requests.get("http://mdg.iitr.ac.in/projects/iitr_chatbot/api/chatbot/Donations/link_to/donation_schemes")
        json_data = response.json()
        url = json_data["url"]
    
        output = "You can get complete information about the schemes under which the alumni can donate at {}".format(url)
        dispatcher.utter_message(text=output)
        return []

class ActionGlobalAlumniNetwork(Action):
    def name(self) -> Text:
        return "action_global_alumni_network"

    def run(self, dispatcher: CollectingDispatcher, 
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text,Any]]:
    
        response = requests.get("http://mdg.iitr.ac.in/projects/iitr_chatbot/api/chatbot/Alumni/global_network/alumni")
        json_data = response.json()
        url = json_data["url"]
    
        output = "You can get complete information about the Global Network for IITR Alumni at {}".format(url)
        dispatcher.utter_message(text=output)
        return []

class ActionDonate(Action):

    def name(self) -> Text:
        return "action_donate"

    def run(self, dispatcher: CollectingDispatcher, 
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text,Any]]:
        
        scheme = tracker.slots.get("scheme_name")
        response = requests.get("http://mdg.iitr.ac.in/projects/iitr_chatbot/api/chatbot/Donations/link_to/how_to_donate")
        json_data = response.json();
        url_how_to_donate = json_data["url"]
        
        if scheme == None:
            scheme = "Schemes"

        output = "The information about how to donate for the {} can be found at the following link: {} \nDetailed Information about the payment procedure can be found at {}".format(scheme,url_how_to_donate, "http://awards.iitr.ac.in/donors/info.php")
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
            response = requests.get("http://mdg.iitr.ac.in/projects/iitr_chatbot/api/chatbot/Alumni/awards/"+map_alumni_awards.get(award))
            json_data = response.json();
            url_award = json_data["url"]
            output = "You can get the information about the {} at {}".format(award,url_award)
        else:
            response = requests.get("http://mdg.iitr.ac.in/projects/iitr_chatbot/api/chatbot/Alumni/awards/"+map_alumni_awards.get("Distinguished Alumni Award"))
            json_data = response.json();
            url_distinguished_alumni_award = json_data["url"]

            response = requests.get("http://mdg.iitr.ac.in/projects/iitr_chatbot/api/chatbot/Alumni/awards/"+map_alumni_awards.get("Outstanding Service Award"))
            json_data = response.json();
            url_outstanding_service_award = json_data["url"]

            response = requests.get("http://mdg.iitr.ac.in/projects/iitr_chatbot/api/chatbot/Alumni/awards/"+map_alumni_awards.get("Research Award"))
            json_data = response.json();
            url_research_award = json_data["url"]

            response = requests.get("http://mdg.iitr.ac.in/projects/iitr_chatbot/api/chatbot/Alumni/awards/"+map_alumni_awards.get("Ramkumar Prize"))
            json_data = response.json();
            url_ramkumar_prize = json_data["url"]

            output = "Distinguished Alumni Award: {}\nOutstanding Service Award: {}\nResearch Award: {}\nRamkumar Prize: {}".format(url_distinguished_alumni_award,url_outstanding_service_award,url_research_award,url_ramkumar_prize)
        dispatcher.utter_message(text=output)
        return []