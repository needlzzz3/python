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
        self.fill_group_form(group)
        # push submit button
        wd.find_element_by_name("submit").click()
        self.retern_group_page()

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field("group_name", group.groupname)
        self.change_field("group_header", group.header)
        self.change_field("group_footer", group.footer)


    def change_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        #подтвердить удаление
        wd.find_element_by_name("delete").click()
        self.retern_group_page()

    def select_first_group(self):
        wd = self.app.wd
        # выбрать первую группу
        wd.find_element_by_name("selected[]").click()

    def modificate_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        wd.find_element_by_xpath("(//input[@name='edit'])").click()
        self.fill_group_form(new_group_data)
        # push update button
        wd.find_element_by_name("update").click()
        self.retern_group_page()

    def retern_group_page(self):
        # retern group page
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))
