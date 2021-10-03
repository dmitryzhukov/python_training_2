# -*- coding: utf-8 -*-

from random import randrange
from fixture import group
from model.group import Group


def test_edit_first_group(app):
    app.group.open_groups_page()
    
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test", footer="test"))

    app.group.open_groups_page()
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="edit group", header="edit header", footer="edit footer")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group)

    app.group.open_groups_page()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
