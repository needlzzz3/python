# -*- coding: utf-8 -*-
import pytest
from group import Group
from app import App


@pytest.fixture
def App(request):
    fixture = app()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(groupname="5555", header="5555", footer="5555"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(groupname="", header="", footer=""))
    app.logout()
