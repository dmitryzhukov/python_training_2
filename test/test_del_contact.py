# -*- coding: utf-8 -*-

from model.contact import Contact
import time

def test_delete_first_contact(app):
    app.contact.open_contact_page()
    app.contact.delete_first_contact()
    time.sleep(1)