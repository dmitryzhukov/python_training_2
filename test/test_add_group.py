# -*- coding: utf-8 -*-

from model.group import Group
import time

def test_add_group(app):
    app.group.open_groups_page()
    app.group.create(Group(name="Test group", header="Test header", footer="Test footer"))
    time.sleep(1)

def test_add_group_empty(app):
    app.group.open_groups_page()
    app.group.create(Group(name="", header="", footer=""))
    time.sleep(1)
