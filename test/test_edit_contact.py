# -*- coding: utf-8 -*-

from model.contact import Contact

def test_edit_first_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
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
    app.open_home_page()
    app.session.logout()
