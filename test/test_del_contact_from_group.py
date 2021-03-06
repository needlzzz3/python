import random

from fixture import group
from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact

orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_del_contact_from_group(app, db):
    groups = db.get_group_list()
    contacts = ddb.get_group_list()
    if len(groups) == 0:
        app.group.create(Group(name="test"))
    if len(contacts) == 0:
        app.contact.contact(Contact(firstname="test"))
    free_groups = db.get_group_list()
    free_contacts = db.get_group_list()
    contacts_in_groups = orm.contacts_in_groups()
    if len(contacts_in_groups) == 0:
        app.contact.add_contact_to_group(free_groups, free_contacts)
        contacts_in_groups = orm.contacts_in_groups()
    contact_n_group = contacts_in_groups[0]
    group_n_contact = orm.get_groups_of_contact(contact_n_group)[0]
    app.contact.remove_contact_from_group(contact_n_group, group_n_contact)
    new_contacts_in_groups = orm.contacts_in_groups()
    assert len(contacts_in_groups) - 1 == len(new_contacts_in_groups)