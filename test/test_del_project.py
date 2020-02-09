from model.project import Project
import pytest
from data.add_project import project
import random


@pytest.mark.parametrize('project', project, ids=[repr(x) for x in project])
def test_del_project(app, project):
    if len(app.project.get_list()) == 0:
        app.project.add_project(project)
    old_projects = app.project.get_list()
    project_to_del = random.choice(old_projects)
    app.project.remove_project_by_id(project_to_del.id)
    new_projects = app.project.get_list()
    old_projects.remove(project_to_del)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
