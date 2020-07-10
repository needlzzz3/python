# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from random import randrange

def test_modificate_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="new")
    group.id = old_groups[index].id
    app.group.modificate_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#def test_modificate_group_header(app):
 #   if app.group.count() == 0:
  #      app.group.create(Group(name="test"))
   # old_groups = app.group.get_group_list()
    #app.group.modificate_first_group(Group(header="666"))
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) == len(new_groups)



