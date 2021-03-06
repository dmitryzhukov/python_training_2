# -*- coding: utf-8 -*-
import random
import time
import pytest

from fixture.application import Application
from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group


@pytest.mark.skip(reason="XAMPP 8 ver")
def test_add_contact_to_group(app: Application, orm: ORMFixture):
    if (len(orm.get_group_list()) == 0):
        app.group.create(Group(name="inital_group"))

    groups = orm.get_group_list()
    random_group = random.choice(groups)

    contacts_not_in_group = orm.get_contacts_not_in_group(random_group)
    if len(contacts_not_in_group) == 0:
        new_contact = Contact(firstname="inital_firstname",
                              lastname="inital_lastname")
        app.contact.create(new_contact)
        contacts_not_in_group = orm.get_contacts_not_in_group(random_group)

    contact_to_attach = contacts_not_in_group[0]
    app.contact.attach_contact_to_group(contact_to_attach, random_group)

    time.sleep(2)
    contacts_in_group = orm.get_contacts_in_group(random_group)

    assert (any(filter(lambda x: x == contact_to_attach, contacts_in_group)))
