class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd  # link for the browser driver
        self.app.open_homepage()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_css_selector("input[type='submit']").click()


    def logout(self):
        wd = self.app.wd  # link for the browser driver
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("username")

    # added to avoid situation when we have closed session before logout    (f.e. extra logout in test_add_group.py)
    def ensure_logout(self):  # check that we closed session
        if self.is_logged_in():  # we get a list of all elements w\ name @Logout
            self.logout()

    # check that we have open session
    def is_logged_in(self):
        wd = self.app.wd  # link for the browser driver
        return len(wd.find_elements_by_link_text("Logout")) > 0

    # check that we have open session w/ needed username
    def is_logged_in_as(self, username):
        # check that we have element "(admin)"
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_css_selector("td.login-info-left span").text

    # added to avoid situation when we have already logged in
    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):  # check that we logged as needed username
                return
            else:
                self.logout()
        self.login(username, password)
