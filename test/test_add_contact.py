# -*- coding: utf-8 -*-


from model.contact import Contact


def test_add_contact(app):
    app.contact.open_contact_page()
    app.contact.create(Contact(firstname="Test First name", middlename="Test Middle name", lastname="Test Last name",
                               nickname="Test Nickname", title="Test Title",
                               company="Test Company", address_company="Test Address", home_phone="Test Home Phone",
                               mobile_phone="Test Mobile Phone", work_phone="Test Work Phone",
                               fax="Test Fax", email="Test@mail.ru", email2="Test2@mail.ru", email3="Test3@mail.ru",
                               homepage="Test Homepage", bday="1",
                               bmonth="January", byear="2000", aday="2", amonth="February", ayear="2010",
                               address="Test Address", home="Test Home",
                               notes="Test Notes"))
