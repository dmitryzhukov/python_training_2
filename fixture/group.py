class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        self.fill_group(group, wd)
        # submit group creation
        wd.find_element_by_name("submit").click()

    def delete_first_group(self):
        wd = self.app.wd
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_name("delete").click()

    def edit_first_group(self, group):
        wd = self.app.wd
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit edition
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group(group, wd)
        # submit group creation
        wd.find_element_by_name("update").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def fill_group(self, group, wd):
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def count(self):
        self.open_groups_page()
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))


