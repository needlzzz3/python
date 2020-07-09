from model.contact import Contact


def test_modification_first_contact(app):
    if app.contact.count() == 0:
        app.contact.contact(Contact (firstname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modificate_first_contact(Contact (firstname="new"))
    new_contacts = app.contact.get_contact_list()
    assert len(new_contacts) == len(old_contacts)