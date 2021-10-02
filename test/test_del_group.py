# -*- coding: utf-8 -*-
import time

def test_delete_first_group(app):
    app.group.open_groups_page()
    app.group.delete_first_group()
    time.sleep(1)