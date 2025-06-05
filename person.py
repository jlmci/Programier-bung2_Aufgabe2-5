import json
from datetime import datetime

class Person:

    def __init__(self, person_dict) -> None:
        self.date_of_birth = person_dict["date_of_birth"]
        self.firstname = person_dict["firstname"]
        self.lastname = person_dict["lastname"]
        self.picture_path = person_dict["picture_path"]
        self.id = person_dict["id"]
    
    @staticmethod
    def load_person_data():
        """A Function that knows where te person Database is and returns a Dictionary with the Persons"""
        file = open("data/person_db.json")
        person_data = json.load(file)
        return person_data

    @staticmethod
    def get_person_list():
        """A Function that takes the persons-dictionary and returns a list auf all person names"""
        person_data = Person.load_person_data()
        list_of_names = []

        for eintrag in person_data:
            list_of_names.append(eintrag["lastname"] + ", " +  eintrag["firstname"])
        return list_of_names
    
    @staticmethod
    def find_person_data_by_name(suchstring):
        """ Eine Funktion der Nachname, Vorname als ein String übergeben wird
        und die die Person als Dictionary zurück gibt"""

        person_data = Person.load_person_data()
        #print(suchstring)
        if suchstring == "None":
            return {}

        two_names = suchstring.split(", ")
        vorname = two_names[1]
        nachname = two_names[0]

        for eintrag in person_data:
            print(eintrag)
            if (eintrag["lastname"] == nachname and eintrag["firstname"] == vorname):
                print()
                return eintrag
        else:
            return {}
        
    
    @staticmethod
    def calc_age(user):
        """Calculate the age of the person based on the date of birth"""
        person_selected = Person.find_person_data_by_name(user)
        date_of_birth = person_selected["date_of_birth"]
        today = datetime.today()
        age = today.year - date_of_birth
        return age
    
    
    def calc_max_hr(self):
        """Calculate the maximum heart rate based on the age of the person"""
        age = self.calc_age()
        max_hr = 220 - age
        return max_hr
    
    @staticmethod
    def load_by_id(person_id):
        """Load a person by ID from the person database"""
        person_data = Person.load_person_data()
        for eintrag in person_data:
            if eintrag['id'] == person_id:
                return eintrag
        return None
    
    def get_ekg_list(currend):
        ''' A function that returns a list of EKG data for the person.'''
        person_used = Person.find_person_data_by_name(currend)
        ekg_list = []
        if len(person_used["ekg_tests"]) >= 1:
            for ekg in person_used["ekg_tests"]:
                ekg_list.append(ekg["id"])
        return ekg_list


        
    

    

if __name__ == "__main__":
    print("This is a module with some functions to read the person data")
    persons = Person.load_person_data()
    person_names = Person.get_person_list(persons)
    #print(persons)
    print(person_names)
    #print(Person.find_person_data_by_name("Huber, Julian"))
    print(Person.load_by_id())
