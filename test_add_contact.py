# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException
import unittest


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.add_contact(wd)
        self.retern_group_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()
        # разлогинились

    def retern_group_page(self, wd):
        wd.find_element_by_link_text("home page").click()
        # вернулись на главную

    def add_contact(self, wd):
        wd.find_element_by_link_text("add new").click()
        # открыли станицу для добавления контактов
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("F")
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("F")
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("F")
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("FFF")
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("FFF")
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("none")
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("none")
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("adress")
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("none")
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("none")
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("none")
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("none")
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("none")
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("none")
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("none")
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("none contact")
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        # добавили контакт

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()
        # залогинились

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/group.php")
        # открыли страницу авторизации

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
