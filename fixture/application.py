from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper


class Application:
    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("unknown %s" % browser)
        # initialize wd variable
        self.wd.implicitly_wait(5)  # not delete because tests are failed
        self.session = SessionHelper(self)  # link to SessionHelper
        self.project = ProjectHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url()
            return True
        except:
            return False

    def open_homepage(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
