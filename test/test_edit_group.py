# -*- coding: utf-8 -*-

from model.group import Group


def test_edit_first_group(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.open_groups_page()
    app.group.edit_first_group(Group(name="edit group", header="edit header", footer="edit footer"))
    app.group.return_to_groups_page()
    app.session.logout()
