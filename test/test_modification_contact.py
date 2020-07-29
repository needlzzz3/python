import random

from fixture import db
from model.contact import Contact


def test_modification_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.contact(Contact(firstname="add"))
    old_contacts = db.get_contact_list()
    contact_old = random.choice(old_contacts)
    id = contact_old.id
    contact = Contact(firstname="add")
    contact.id = id
    app.contact.modificate_contact_by_id(id, contact)
    new_contacts = db.get_contact_list()
    for i in range(len(old_contacts)):
        if old_contacts[i].id == id:
            old_contacts[i] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)