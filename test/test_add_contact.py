# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.app import App


@pytest.fixture
def app(request):
    fixture = App()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
        app.session.login(username="admin", password="secret")
        app.contact.contact(Contact (firstname="F", middlename="F", lastname="F", nickname="FFF", title="FFF", company= "none", address="none", home="adress", mobile="none",
                         work="none", fax="none", email= "none", email2="none", address2="none", phone2="none", notes="none contact"))
        app.session.logout()

def test_add_empty_contact(app):
        app.session.login(username="admin", password="secret")
        app.contact.contact(Contact (firstname="a", middlename="a", lastname="a", nickname="", title="", company="",
                         address="", home="", mobile="",
                         work="", fax="", email="", email2="", address2="", phone2="",
                         notes="empty contact"))
        app.session.logout()
