# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.app import App


@pytest.fixture
def app(request):
    fixture = App()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(groupname="5555", header="5555", footer="5555"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(groupname="", header="", footer=""))
    app.session.logout()