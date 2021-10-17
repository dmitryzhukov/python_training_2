# -*- coding: utf-8 -*-

import pytest
from data.data import test_contacts
from model.contact import Contact


@pytest.mark.parametrize("contact", test_contacts, ids=[repr(x) for x in test_contacts])
def test_add_contact(app, contact):
    app.contact.open_contact_page()

    old_contacts = app.contact.get_contact_list()

    # contact = Contact(firstname="Test First name", middlename="Test Middle name", lastname="Test Last name",
    #                   nickname="Test Nickname", title="Test Title",
    #                   company="Test Company", address_company="Test Address", home_phone="Test Home Phone",
    #                   mobile_phone="Test Mobile Phone", work_phone="Test Work Phone",
    #                   fax="Test Fax", email="Test@mail.ru", email2="Test2@mail.ru", email3="Test3@mail.ru",
    #                   homepage="Test Homepage", bday="1",
    #                   bmonth="January", byear="2000", aday="2", amonth="February", ayear="2010",
    #                   address="Test Address", home="Test Home",
    #                   notes="Test Notes")

    app.contact.create(contact)

    app.contact.open_contact_page()

    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(
        new_contacts, key=Contact.id_or_max)
