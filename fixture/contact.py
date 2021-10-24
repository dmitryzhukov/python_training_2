from model.contact import Contact
from model.group import Group
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select


class ContactHelper:
    contacts_cache = None

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/")):
            wd.get("http://localhost/addressbook/")

    def deattach_contact_from_group(self, contact: Contact, group: Group):
        wd = self.app.wd
        self.open_contact_page()
        Select(wd.find_element_by_css_selector(
            "select[name='group']")).select_by_value(group.id)
        self.select_contact_by_id(contact.id)
        wd.find_element_by_css_selector("input[name='remove']").click()

    def attach_contact_to_group(self, contact: Contact, group: Group):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_id(contact.id)
        Select(wd.find_element_by_css_selector(
            "select[name='to_group']")).select_by_value(group.id)
        wd.find_element_by_css_selector("input[name='add']").click()
        self.open_contact_page()

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_contact(contact)
        # click Enter
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.reset_cache()

    def reset_cache(self):
        self.contacts_cache = None

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(0, contact)

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        # select first contact
        wd.find_elements_by_css_selector(
            "tr[name='entry'] img[title='Edit']")[index].click()
        # fill contact form
        self.fill_contact(contact)
        # submit update
        wd.find_element_by_name("update").click()
        self.reset_cache()

    def open_edit_page_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_css_selector(
            "a[href='edit.php?id=%s']" % id).click()

    def edit_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.open_contact_page()
        self.open_edit_page_by_id(id)
        # fill group form
        self.fill_contact(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.reset_cache()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        # select first contact
        wd.find_elements_by_name("selected[]")[index].click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.reset_cache()

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.reset_cache()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def set_field_value(self, key, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(key).click()
            wd.find_element_by_name(key).clear()
            wd.find_element_by_name(key).send_keys(value)

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def fill_contact(self, contact):
        wd = self.app.wd
        self.set_field_value("firstname", contact.firstname)
        self.set_field_value("middlename", contact.middlename)
        self.set_field_value("lastname", contact.lastname)
        self.set_field_value("nickname", contact.nickname)
        self.set_field_value("company", contact.company)

        self.set_field_value("address", contact.address_company)
        self.set_field_value("home", contact.home_phone)
        self.set_field_value("mobile", contact.mobile_phone)
        self.set_field_value("work", contact.work_phone)
        self.set_field_value("fax", contact.fax)
        self.set_field_value("email", contact.email)
        self.set_field_value("email2", contact.email2)
        self.set_field_value("email3", contact.email3)
        self.set_field_value("homepage", contact.homepage)

        self.set_field_value("byear", contact.byear)

        self.set_field_value("address2", contact.address)
        self.set_field_value("phone2", contact.home)
        self.set_field_value("notes", contact.notes)

        if contact.group_id is not None:
            Select(wd.find_element_by_css_selector(
                "select[name='new_group']")).select_by_value(contact.group_id)

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd

        if self.contacts_cache is None:
            self.contacts_cache = []

            for element in wd.find_elements_by_css_selector("tr[name='entry']"):
                cells = element.find_elements_by_tag_name("td")
                id = element.find_element_by_name(
                    "selected[]").get_attribute("value")
                name = cells[2].text
                surname = cells[1].text
                all_phones = cells[5].text
                all_emails = cells[4].text
                address = cells[3].text
                self.contacts_cache.append(
                    Contact(firstname=name, id=id, lastname=surname, all_phones=all_phones, all_emails=all_emails,
                            address=address))

        return list(self.contacts_cache)

    def open_contact_to_edit_by_index(self, index: int):
        wd = self.app.wd
        self.open_contact_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def get_from_edit_page(self, index: int):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        secondary_phone = wd.find_element_by_name(
            "phone2").get_attribute("value")

        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")

        address = wd.find_element_by_name("address").get_attribute("value")

        return Contact(firstname=firstname, lastname=lastname, id=id, home_phone=home_phone, work_phone=work_phone,
                       mobile_phone=mobile_phone, secondary_phone=secondary_phone,
                       email=email, email2=email2, email3=email3, address=address)
