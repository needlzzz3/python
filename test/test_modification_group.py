# -*- coding: utf-8 -*-
import pytest
from model.group import Group

def test_modificate_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modificate_group(Group(groupname="666", header="666", footer="666"))
    app.session.logout()



