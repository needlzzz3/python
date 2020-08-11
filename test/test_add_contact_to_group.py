from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group
from fixture import orm
import random




db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")



def test_add_contact_to_group(app, db):
    groups = db.get_group_list()
    if len(groups) == 0:
        app.group.create(Group(name="test"))
        new_groups = db.get_group_list()
    group = random.choice(groups)
    contacts = db.contacts_without_groups()
    if len(contacts) == 0:
        app.contact.contact(Contact(firstname="test"))
        new_contacts = db.contacts_without_groups()
    contact = random.choice(contacts)
    app.contact.add_contact_to_group(contact, group)
    assert len(contacts) == len(new_contacts) + 1
    assert len(groups) == len(new_groups) + 1