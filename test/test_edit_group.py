# -*- coding: utf-8 -*-

from model.group import Group


def test_edit_first_group(app):
    app.group.open_groups_page()
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test", footer="test"))

    app.group.open_groups_page()
    app.group.edit_first_group(Group(name="edit group", header="edit header", footer="edit footer"))
