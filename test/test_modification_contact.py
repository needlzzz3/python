from model.contact import Contact
from random import randrange


def test_modification_contact(app):
    if app.contact.count() == 0:
        app.contact.contact(Contact(firstname="add"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="add")
    contact.id = old_contacts[index].id
    app.contact.modificate_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(new_contacts) == len(old_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
