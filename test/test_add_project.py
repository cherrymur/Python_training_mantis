from model.project import Project
import pytest
from data.add_project import project


@pytest.mark.parametrize('project', project, ids=[repr(x) for x in project])
def test_add_project(app, project):
    web_config = app.config['web']
    username = web_config['username']
    password = web_config['password']
    old_projects = app.soap.get_list(username, password)  # app.project.get_list()
    app.project.add_project(project)
    new_projects = app.soap.get_list(username, password)
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
