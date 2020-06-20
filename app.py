from selenium import webdriver

class App:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def open_home_page(self):
        # open main page
        wd = self.wd
        wd.get("http://localhost/addressbook/group.php")

    def login(self, username, password):
        # login
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        # push login button
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_group_page(self):
        # go to group page
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def create_group(self, Group):
        # create group
        wd = self.wd
        self.open_group_page()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(Group.groupname)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(Group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(Group.footer)
        # push submit button
        wd.find_element_by_name("submit").click()
        self.retern_group_page()

    def retern_group_page(self):
        # retern group page
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def logout(self):
        # logout
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def destroy(self):
        self.wd.quit()
