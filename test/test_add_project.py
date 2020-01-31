from model.project import Project

new_project = Project(name="new_pr", status="new_st", view_state="new_state", description="new_descr")


def test_add_project(app):
    global new_project
    old_projects = app.project.get_list()
    app.project.add_project(new_project)
    new_projects = app.project.get_list()
    old_projects.append(new_project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)