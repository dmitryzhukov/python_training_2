from model.contact import Contact
from fixture.string_generator import random_string

test_contacts = [
    Contact(firstname=random_string("name", 10), lastname=random_string(
            "last_name", 10), middlename=random_string("middle_name", 10))
    for i in range(5)
]
