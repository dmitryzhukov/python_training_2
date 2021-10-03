# -*- coding: utf-8 -*-
import time
from model.group import Group


def test_delete_first_group(app):
    app.group.open_groups_page()

    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test", footer="test"))

    app.group.open_groups_page()
    app.group.delete_first_group()
    time.sleep(1)