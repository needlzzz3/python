class GroupHelper:

    def __init__ (self, app):
        self.app = app

    def open_group_page(self):
        # go to group page
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        # create group
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.groupname)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # push submit button
        wd.find_element_by_name("submit").click()
        self.retern_group_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        #выбрать первую группу
        wd.find_element_by_name("selected[]").click()
        #подтвердить удаление
        wd.find_element_by_name("delete").click()
        self.retern_group_page()

    def modificate_group(self, group):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("(//input[@name='edit'])").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.groupname)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # push update button
        wd.find_element_by_name("update").click()
        self.retern_group_page()


    def retern_group_page(self):
        # retern group page
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()