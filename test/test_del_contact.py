# -*- coding: utf-8 -*-

from model.contact import Contact


def test_delete_first_contact(app):
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

    app.contact.open_contact_page()
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()

    app.contact.open_contact_page()
    new_contacts = app.contact.get_contact_list()

    old_contacts.pop(0)

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)