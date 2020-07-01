# -*- coding: utf-8 -*-
import pytest
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(groupname="5555", header="5555", footer="5555"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(groupname="", header="", footer=""))
    app.session.logout()
