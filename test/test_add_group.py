# -*- coding: utf-8 -*-

from fixture.application import Application
from model.group import Group

import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.open_groups_page()
    app.group.create(Group(name="Test group", header="Test header", footer="Test footer"))
    app.group.return_to_groups_page()
    app.session.logout()


def test_add_group_empty(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.open_groups_page()
    app.group.create(Group(name="", header="", footer=""))
    app.group.return_to_groups_page()
    app.session.logout()


