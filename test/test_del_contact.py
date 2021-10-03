# -*- coding: utf-8 -*-

from model.contact import Contact

def test_delete_first_group(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.open_contact_page()
    app.contact.delete_first_contact()
    app.open_home_page()
    app.session.logout()
