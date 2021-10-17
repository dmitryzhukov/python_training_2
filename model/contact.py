from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None, address_company=None, home_phone=None,
                 mobile_phone=None, work_phone=None, fax=None, email=None, email2=None, email3=None, homepage=None, bday=None, bmonth=None,
                 byear=None, aday=None, amonth=None, ayear=None, address=None, home=None, notes=None, id=None, secondary_phone=None, all_phones=None,
                 all_emails=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address_company = address_company
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address = address
        self.home = home
        self.notes = notes
        self.id = id
        self.secondary_phone = secondary_phone
        self.all_phones = all_phones
        self.all_emails = all_emails

    def __repr__(self):
        return f"{self.id}:{self.firstname}:{self.lastname}"

    def __eq__(self, other) -> bool:
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname and self.address == other.address

    def id_or_max(contact):
        if contact.id:
            return int(contact.id)
        else:
            return maxsize
