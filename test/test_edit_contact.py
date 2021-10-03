# -*- coding: utf-8 -*-

from model.contact import Contact
import time


def test_edit_first_contact(app):
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
    app.contact.edit_first_contact(Contact(firstname="Edit First name", middlename="Edit Middle name", lastname="Edit Last name",
                               nickname="Edit Nickname", title="Edit Title",
                               company="Edit Company", address_company="Edit Address", home_phone="Edit Home Phone",
                               mobile_phone="Edit Mobile Phone", work_phone="Edit Work Phone",
                               fax="Edit Fax", email="Edit@mail.ru", email2="Edit2@mail.ru", email3="Edit3@mail.ru",
                               homepage="Edit Homepage", bday="1",
                               bmonth="January", byear="2000", aday="2", amonth="February", ayear="2010",
                               address="Edit Address", home="Edit Home",
                               notes="Edit Notes"))
    time.sleep(1)
