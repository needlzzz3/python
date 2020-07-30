import pymysql.cursors

from model import contact
from model.group import Group
from model.contact import Contact
import re


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def removing_spaces(self, s):
        return re.sub("  ", " ", s.strip())

    def merge_phones_like_on_home_page(self, contacts):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: self.clear(x),
                                    filter(lambda x: x is not None,
                                           [contact.home, contact.mobile, contact.work, contact.phone2]))))

    def merge_emails_like_on_home_page(self, contacts):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: self.clear(x),
                                    filter(lambda x: x is not None,
                                           [contact.email, contact.email2, contact.email3]))))

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, email, email2, email3, home, mobile, work, phone2 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, email, email2, email3, home, mobile, work, phone2) = row
                current_contact = Contact(id=str(id), lastname=lastname, firstname=firstname, address=address, email=email, email2=email2, email3=email3,
                                    home=home, mobile=mobile, work=work, phone2=phone2)
                final_contact = Contact(id=str(id), lastname=self.removing_spaces(lastname), firstname=self.removing_spaces(firstname), address=self.removing_spaces(address), email=self.removing_spaces(email), email2=self.removing_spaces(email2), email3=self.removing_spaces(email3),
                                    home=self.removing_spaces(home), mobile=self.removing_spaces(mobile), work=self.removing_spaces(work), phone2=self.removing_spaces(phone2))
                final_contact.all_phones_from_home_page = self.merge_phones_like_on_home_page(current_contact)
                final_contact.all_emails_from_home_page = self.merge_emails_like_on_home_page(current_contact)
                list.append(final_contact)
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()