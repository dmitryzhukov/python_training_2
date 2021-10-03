# -*- coding: utf-8 -*-

from model.group import Group

def test_add_group(app):
    app.group.open_groups_page()

    old_groups = app.group.get_group_list()

    group = Group(name="Test group", header="Test header", footer="Test footer")
    app.group.create(group)

    app.group.open_groups_page()

    new_groups = app.group.get_group_list()
    old_groups.append(group)

    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_group_empty(app):
    app.group.open_groups_page()

    old_groups = app.group.get_group_list()

    group = Group(name="", header="", footer="")
    app.group.create(group)

    app.group.open_groups_page()

    new_groups = app.group.get_group_list()
    old_groups.append(group)

    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
