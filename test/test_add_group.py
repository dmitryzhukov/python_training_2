# -*- coding: utf-8 -*-

import pytest
from model.group import Group
from data.data import test_grops


def test_add_group(app, json_groups):
    group = json_groups
    app.group.open_groups_page()

    old_groups = app.group.get_group_list()

    app.group.create(group)

    app.group.open_groups_page()

    new_groups = app.group.get_group_list()
    old_groups.append(group)

    assert sorted(old_groups, key=Group.id_or_max) == sorted(
        new_groups, key=Group.id_or_max)
