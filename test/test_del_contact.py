# -*- coding: utf-8 -*-

from model.contact import Contact
import random
import time


def test_delete_first_contact(app, db, check_ui):
    app.contact.open_contact_page()

    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test First name", middlename="Test Middle name", lastname="Test Last name",
                                   nickname="Test Nickname", title="Test Title",
                                   company="Test Company", address_company="Test Address", home_phone="Test Home Phone",
                                   mobile_phone="Test Mobile Phone", work_phone="Test Work Phone",
                                   fax="Test Fax", email="Test@mail.ru", email2="Test2@mail.ru", email3="Test3@mail.ru",
                                   homepage="Test Homepage", bday="1",
                                   bmonth="January", byear="2000", aday="2", amonth="February", ayear="2010",
                                   address="Test Address", home="Test Home",
                                   notes="Test Notes"))

    old_contacts = db.get_contact_list()
    contact_to_delete = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact_to_delete.id)
    time.sleep(1)
    new_contacts = db.get_contact_list()

    old_contacts.remove(contact_to_delete)

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(
        new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(
            app.contact.get_contact_list(), key=Contact.id_or_max)
