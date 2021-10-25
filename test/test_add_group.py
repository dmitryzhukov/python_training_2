# -*- coding: utf-8 -*-

import pytest
from model.group import Group
from data.data import test_grops
import allure


def test_add_group(app, db,  json_groups, check_ui):
    group = json_groups
    app.group.open_groups_page()
    with allure.step('Given a group list'):
        old_groups = db.get_group_list()
    with allure.step('When i add a group %s to the list' % group):
        app.group.create(group)
    with allure.step('Then the new group list is equal to the old list with the added group'):
        app.group.open_groups_page()

    new_groups = db.get_group_list()
    old_groups.append(group)

    assert sorted(old_groups, key=Group.id_or_max) == sorted(
        new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
