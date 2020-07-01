# -*- coding: utf-8 -*-
import pytest
from model.group import Group

def test_modificate_group_name(app):
    app.group.modificate_first_group(Group(groupname="666"))

def test_modificate_group_header(app):
    app.group.modificate_first_group(Group(header="666"))



