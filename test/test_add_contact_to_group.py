from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group
from fixture import orm
import random




orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")



def test_add_contact_to_group(app, db):
    groups = db.get_group_list()
    contacts = db.get_contact_list()
    if len(groups) == 0:
        app.group.create(Group(name="test"))
    if len(contacts) == 0:
        app.contact.contact(Contact(firstname="test"))
    contacts_without_groups = orm.contacts_without_groups()
    app.contact.add_contact_to_group()
    new_contacts_without_groups = orm.contacts_without_groups()
    assert len(contacts_without_groups)-1 == len(new_contacts_without_groups)