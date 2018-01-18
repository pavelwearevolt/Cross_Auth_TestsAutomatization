__author__ = 'pavelkosicin'

import time


class ValidationHelper:

    def __init__(self, app):
        self.app = app

    def enter_wrong_data(self, username, password):
        wd = self.app.wd
        self.app.navigation.open_cross_auth_page()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(username)
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_css_selector("button.btn.btn-default.btn-block").click()

    def check_empty_data_error_message(self):
        wd = self.app.wd
        # check email validation error message
        assert wd.find_element_by_xpath("//*[@id='action-form']/div[1]/div[1]/div/span/div"), "No error message"
        email_message_text = wd.find_element_by_xpath("//*[@id='action-form']/div[1]/div[1]/div/span/div").text
        assert email_message_text == "Invalid email", "Wrong text in error message"
        # check password validation error message
        assert wd.find_element_by_xpath("//*[@id='action-form']/div[1]/div[2]/div/span/div"), "No error message"
        email_message_text = wd.find_element_by_xpath("//*[@id='action-form']/div[1]/div[2]/div/span/div").text
        assert email_message_text == "Invalid password", "Wrong text in error message"

    def check_invalid_email_short_password_error_message(self):
        wd = self.app.wd
        # check invalid email validation error message
        assert wd.find_element_by_xpath("//*[@id='action-form']/div[1]/div[1]/div/span/div"), "No error message"
        email_message_text = wd.find_element_by_xpath("//*[@id='action-form']/div[1]/div[1]/div/span/div").text
        assert email_message_text == "Invalid email", "Wrong text in error message"
        # check short password validation error message
        assert wd.find_element_by_xpath("//*[@id='action-form']/div[1]/div[2]/div/span/div"), "No error message"
        email_message_text = wd.find_element_by_xpath("//*[@id='action-form']/div[1]/div[2]/div/span/div").text
        assert email_message_text == "Password must be at least 8 characters long", "Wrong text in error message"

    def check_wrong_data(self):
        wd = self.app.wd
        # check wrong email and password validation error message
        assert wd.find_element_by_xpath("//*[@id='action-form']/div[1]/div[3]/span/div"), "No error message"
        email_message_text = wd.find_element_by_xpath("//*[@id='action-form']/div[1]/div[3]/span/div").text
        assert email_message_text == "Dagnabbit! It seems you've entered the wrong email and/or password. Please try again", "Wrong text in error message"
