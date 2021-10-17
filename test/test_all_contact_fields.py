# -*- coding: utf-8 -*-

from fixture.application import Application
from random import randrange
import re

from model.contact import Contact


def test_all_contact_fields(app: Application):
    count = app.contact.count()

    index = randrange(count)
    contact_from_list = app.contact.get_contact_list()[index]
    contact_from_edit = app.contact.get_from_edit_page(index)
    assert contact_from_list == contact_from_edit

    expected_phones = contact_from_list.all_phones
    actual_phones = merge_phones_like_on_home_page(
        contact_from_edit)
    assert expected_phones == actual_phones

    expected_emails = contact_from_list.all_emails
    actual_emails = merge_emails_like_on_home_page(contact_from_edit)
    assert expected_emails == actual_emails

    assert contact_from_list.address == contact_from_edit.address


def clear_phones(s):
    return re.sub("[() -]", "", s)


def clear_emails(s):
    return re.sub("\s+", " ", s)


def merge_emails_like_on_home_page(contact: Contact):
    return "\n".join(
        filter(lambda x: x != "",
            map(clear_emails,
                filter(lambda x: x is not None,
                    [contact.email, contact.email2, contact.email3]))))


def merge_phones_like_on_home_page(contact: Contact):
    return "\n".join(
        filter(lambda x: x != "",
               map(clear_phones,
                   filter(lambda x: x is not None,
                          [contact.home_phone, contact.mobile_phone, contact.work_phone, contact.secondary_phone]))))
