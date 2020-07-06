# -*- coding: utf-8 -*-
import pytest
from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(groupname="5555", header="5555", footer="5555"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) +1 == len(new_groups)




def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(groupname="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


