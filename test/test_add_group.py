# -*- coding: utf-8 -*-
import pytest
from model.group import Group


def test_add_group(app):
    if app.group.count() == 0:
        app.group.create(Group(groupname="5555", header="5555", footer="5555"))
    else:
        pass



def test_add_empty_group(app):
    if app.group.count() == 0:
        app.group.create(Group(groupname="", header="", footer=""))
    else:
        pass

