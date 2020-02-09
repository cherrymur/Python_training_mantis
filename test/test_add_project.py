from model.project import Project
import pytest
from data.add_project import project


@pytest.mark.parametrize('project', project, ids=[repr(x) for x in project])
def test_add_project(app, project):
    old_projects = app.project.get_list()
    app.project.add_project(project)
    new_projects = app.project.get_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
