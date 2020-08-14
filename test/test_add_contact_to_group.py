from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group
from fixture import orm
import random




orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")



def test_add_contact_to_group(app, db):
    groups = db.get_group_list()
    contacts = db.get_group_list()
    if len(groups) == 0:
        app.group.create(Group(name="test"))
    if len(contacts) == 0:
        app.contact.contact(Contact(firstname="test"))
    free_groups = orm.get_group_list()
    free_contacts = orm.get_group_list()
    app.contact.add_contact_to_group(free_groups[0], free_contacts[0])
    new_free_groups = orm.get_group_list()
    new_free_contacts = orm.get_group_list()
    assert len(free_contacts) == len(new_free_contacts) - 1
    assert len(free_groups) == len(new_free_groups) - 1