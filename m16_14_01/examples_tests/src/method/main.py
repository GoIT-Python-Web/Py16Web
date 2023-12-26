import json


def write_contacts_to_file(filename, contacts):
    with open(filename, "w") as file:  #
        json.dump({"contacts": contacts}, file)  #


def read_contacts_from_file(filename):
    with open(filename, "r") as file:  #
        content = json.load(file)  #
    return content.get("contacts")  #
