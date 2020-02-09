
from suds.client import Client
from suds import WebFault

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = self.get_info_link()
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_info_link(self):
        return Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")

    def get_list(self, app, username, password, id):
        client = self.get_info_link()
        list_ids = app.project.get_list_id()
        try:
            for i in list_ids:
                projects += client.service.mc_filter_get(username, password, id)
            return list(projects)
        except WebFault:
            return False

    def add_project(self, username, password, project):
        client = self.get_info_link()
        try:
            new_project = client.service.mc_project_add(username, password, project)
            return list(new_project)
        except WebFault:
            return False