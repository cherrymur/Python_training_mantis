from model.project import Project
import pytest
from data.add_project import project


@pytest.mark.parametrize('project', project, ids=[repr(x) for x in project])
def test_add_project(app, project):
    web_config = app.config['web']
    username = web_config['username']
    password = web_config['password']
    list_ids = app.project.get_list_id()
    old_projects = []
    for id in list_ids:
        old_projects += app.soap.get_list(username, password, id)
    app.project.add_project(project)
    new_projects = app.soap.get_list(username, password)
    list_ids.append(project)
    assert sorted(list_ids, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
