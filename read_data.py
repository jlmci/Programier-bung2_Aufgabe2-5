import json

def load_person_data():
    """A Function that knows where the person database is and returns a dictionary with the persons"""
    file = open("data/person_db.json")
    person_data = json.load(file)
    return person_data


def create_name_list():
    """A Function that knows where the person database is and returns a dictionary with the persons"""
    file = open("data/person_db.json")
    person_data = json.load(file)
    
    #Extract the name of each person in person_data and put in in a list
    namen_liste = [f"{person['firstname']} {person['lastname']}" for person in person_data]
    return namen_liste

def get_person_data_ba_name(person_data, name_to_find):
    name_to_find = name_to_find.strip()
    name_to_find.split(", ")
    
    for i in person_data:
        # Check if the name_to_find is in the firstname or lastname of the person
        if name_to_find[0] in i["firstname"] and name_to_find[1] in i["lastname"]:
            return i

    return None




if __name__ == "__main__":
    # This is the main function that will be executed when the script is run
    person_data = load_person_data()
    person_name_list = create_name_list()
    print("Person data loaded successfully.")
    print(person_data)
    print(person_name_list)
    print("Picture path: ", picture_path(person_data))