# -*- coding: utf-8 -*-

import time
import random
from fixture import group
from model.group import Group


def test_edit_first_group(app, db, check_ui):
    app.group.open_groups_page()

    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test", footer="test"))

    app.group.open_groups_page()
    old_groups = db.get_group_list()
    group_to_edit = random.choice(old_groups)
    group = Group(name="edit group", header="edit header",
                  footer="edit footer", id=group_to_edit.id)
    app.group.edit_group_by_id(group_to_edit.id, group)

    time.sleep(2)
    new_groups = db.get_group_list()
    old_groups[old_groups.index(group_to_edit)] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(
        new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(
            app.group.get_group_list(), key=Group.id_or_max)
