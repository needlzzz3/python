from model.contact import Contact


def test_modification_first_contact(app):
    if app.contact.count() == 0:
        app.contact.contact(Contact (firstname="test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact (firstname="new")
    contact.id = old_contacts[0].id
    app.contact.modificate_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(new_contacts) == len(old_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

