from model.group import Group


class GroupHelper:

    groups_cache = None

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        # init group creation
        self.open_groups_page()
        wd.find_element_by_name("new").click()
        # fill group form
        self.fill_group(group, wd)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.reset_cache()

    def delete_group_by_index(self, index):
        wd = self.app.wd
        # select first group
        wd.find_elements_by_name("selected[]")[index].click()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.reset_cache()

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.reset_cache()

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def edit_group_by_index(self, index, group):
        wd = self.app.wd
        # select first group
        wd.find_elements_by_name("selected[]")[index].click()
        # submit edition
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group(group, wd)
        # submit group creation
        wd.find_element_by_name("update").click()
        self.reset_cache()

    def edit_group_by_id(self, id, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        # open modification form
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group(new_group_data, wd)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.reset_cache()

    def edit_first_group(self, group):
        self.edit_group_by_index(0, group)

    def reset_cache(self):
        self.groups_cache = None

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def fill_group(self, group, wd):
        self.set_field_value("group_name", group.name)
        self.set_field_value("group_header", group.header)
        self.set_field_value("group_footer", group.footer)

    def set_field_value(self, key, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(key).click()
            wd.find_element_by_name(key).clear()
            wd.find_element_by_name(key).send_keys(value)

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    def get_group_list(self):
        wd = self.app.wd

        if self.groups_cache is None:
            self.groups_cache = []

            for element in wd.find_elements_by_css_selector("span.group"):
                groupName = element.text
                groupId = element.find_element_by_name(
                    "selected[]").get_attribute("value")
                self.groups_cache.append(Group(name=groupName, id=groupId))

        return list(self.groups_cache)
