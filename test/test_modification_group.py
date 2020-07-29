# -*- coding: utf-8 -*-
import random

import pytest

from fixture import db
from model.group import Group
import random


def test_modificate_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group_old = random.choice(old_groups)
    id = group_old.id
    group_new = Group(id=id, name="test", header="test", footer="test")
    app.group.modificate_group_by_id(id, group_new)
    new_groups = db.get_group_list()
    for i in range(len(old_groups)):
        if old_groups[i].id == id:
            old_groups[i] = group_new
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

#def test_modificate_group_header(app):
 #   if app.group.count() == 0:
  #      app.group.create(Group(name="test"))
   # old_groups = app.group.get_group_list()
    #app.group.modificate_first_group(Group(header="666"))
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) == len(new_groups)



