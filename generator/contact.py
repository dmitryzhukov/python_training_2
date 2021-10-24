import getopt
import os.path
import sys

import jsonpickle
from fixture.string_generator import random_string
from model.contact import Contact

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", [
                               "number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 2
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


testdata = [Contact(firstname="", lastname="")] + [
    Contact(firstname=random_string("firstname", 6),
            lastname=random_string("lastname", 8))
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
