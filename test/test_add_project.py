from model.project import Project
import string
import random

'''
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

new_project = [
    Project(name=name, description=description)
    for name in ["", random_string("name", 10)]
    for description in ["", random_string("description", 10)]
]'''
new_project = Project(name="New Project",
                             description="Project Description")

def test_add_project(app):
    global new_project
    old_projects = app.project.get_list()
    app.project.add_project(new_project)
    new_projects = app.project.get_list()
    old_projects.append(new_project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
