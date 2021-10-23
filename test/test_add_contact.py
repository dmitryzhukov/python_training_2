# -*- coding: utf-8 -*-

import pytest
from data.data import test_contacts
from model.contact import Contact


def test_add_contact(app, json_contacts):
    contact = json_contacts
    app.contact.open_contact_page()

    old_contacts = app.contact.get_contact_list()

    app.contact.create(contact)

    app.contact.open_contact_page()

    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(
        new_contacts, key=Contact.id_or_max)
