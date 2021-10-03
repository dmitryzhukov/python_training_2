# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    app.group.open_groups_page()
    app.group.create(Group(name="Test group", header="Test header", footer="Test footer"))

def test_add_group_empty(app):
    app.group.open_groups_page()
    app.group.create(Group(name="", header="", footer=""))
