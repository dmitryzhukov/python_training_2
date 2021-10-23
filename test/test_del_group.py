# -*- coding: utf-8 -*-
import random
import time
from model.group import Group
from random import randrange


def test_delete_first_group(app, db, check_ui):
    app.group.open_groups_page()

    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test", footer="test"))

    app.group.open_groups_page()
    old_groups = db.get_group_list()

    group_to_delete = random.choice(old_groups)
    app.group.delete_group_by_id(group_to_delete.id)

    time.sleep(2)
    new_groups = db.get_group_list()
    old_groups.remove(group_to_delete)

    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
