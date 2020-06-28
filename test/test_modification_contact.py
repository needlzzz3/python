from model.contact import Contact


def test_delete_first_contact(app):
    app.session.login (username="admin", password="secret")
    app.contact.modificate_contact(Contact (firstname="c", middlename="c", lastname="c", nickname="c", title="c", company="c",
                                address="c", home="c", mobile="c",
                                work="c", fax="c", email="c", email2="c", address2="c", phone2="c",
                                notes="modificated"))
    app.session.logout()