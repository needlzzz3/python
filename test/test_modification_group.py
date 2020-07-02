# -*- coding: utf-8 -*-
import pytest
from model.group import Group

def test_modificate_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(groupname="test"))
    app.group.modificate_first_group(Group(groupname="666"))

def test_modificate_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(groupname="test"))
    app.group.modificate_first_group(Group(header="666"))



