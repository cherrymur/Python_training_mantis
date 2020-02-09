from selenium.webdriver.support.select import Select

from model.project import Project


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def add_project(self, project):
        wd = self.app.wd
        self.open_create_page()
        self.fill_form(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.open_manage_page()
        self.project_cache = None

    def open_manage_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("manage_proj_page.php")):
            wd.get("http://localhost/mantisbt-1.2.20/manage_proj_page.php")

    def change_each_form(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            try:
                wd.find_element_by_name(field_name).click()
                wd.find_element_by_name(field_name).clear()
                wd.find_element_by_name(field_name).send_keys(text)
            except:
                Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def fill_form(self, project):
        self.change_each_form("name", project.name)
        self.change_each_form("status", project.status)
        self.change_each_form("view_state", project.view_state)
        self.change_each_form("description", project.description)

    def open_create_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("manage_proj_create_page.php")):
            wd.get("http://localhost/mantisbt-1.2.20/manage_proj_create_page.php")

    project_cache = None

    def get_list(self):
        wd = self.app.wd
        if self.project_cache is None:
            self.open_manage_page()
            self.project_cache = []
            elements = wd.find_elements_by_css_selector("table.width100 tr.row-1")
            elements += wd.find_elements_by_css_selector("table.width100 tr.row-2")
            for element in elements:
                graphs = element.find_elements_by_tag_name('td')
                name = graphs[0].text
                status = graphs[1].text
                view_state = graphs[3].text
                description = graphs[4].text
                id_link = wd.find_element_by_partial_link_text(name).get_attribute("href")
                id_index = id_link.index('=') + 1
                id = id_link[id_index:]
                self.project_cache.append(Project(id=id, name=name, status=status, view_state=view_state,
                                                  description=description))
        return list(self.project_cache)

