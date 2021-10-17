from model.contact import Contact
from fixture.string_generator import random_string
from model.group import Group

test_contacts = [Contact(firstname="", middlename="", lastname="")] + [
    Contact(firstname=random_string("name", 10), lastname=random_string(
            "last_name", 10), middlename=random_string("middle_name", 10))
    for i in range(5)
]

test_grops = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string(
        "header", 15), footer=random_string("footer", 15))
    for i in range(5)
]
