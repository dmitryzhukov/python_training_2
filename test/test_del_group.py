# -*- coding: utf-8 -*-

from model.group import Group


def test_delete_first_group(app):
    app.group.open_groups_page()

    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test", footer="test"))

    app.group.open_groups_page()
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()

    app.group.open_groups_page()
    new_groups = app.group.get_group_list()

    old_groups.pop(0)

    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
