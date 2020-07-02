from model.contact import Contact


def test_modification_first_contact(app):
    if app.contact.count() == 0:
        app.contact.contact(Contact (firstname="test"))
    app.contact.modificate_first_contact(Contact (firstname="new"))