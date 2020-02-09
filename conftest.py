# Create common fixture
from fixture.application import Application  # group.py - package group, Group - module
import json
import os.path
import pytest
import ftputil


fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


@pytest.fixture(scope="session")
def config(request):
    return load_config(request.config.getoption("--target"))

# intialization fixture before each test
@pytest.fixture
def app(request, config):
    global fixture
    browser = request.config.getoption("--browser")
    if fixture is None or not fixture.is_valid():  # check that fixture not exists
        fixture = Application(browser=browser, base_url=config['web']['baseUrl'])
        fixture.session.ensure_login(username=config['web']['username'], password=config['web']['password'])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def configure_server(request, config):
    install_server_configuration(config['ftp']['host'], config['ftp']['username'], config['ftp']['password'])
    def fin():
        restore_server_configuration(config['ftp']['host'], config['ftp']['username'], config['ftp']['password'])
    request.addfinalizer(fin)


def install_server_configuration(host, username, password):
    with ftputil.FTPHost(host, username, password) as remote:
        if remote.path.isfile("config_inc.php.back"):
            remote.remove("config_inc.php.back")
        if remote.path.isfile("config_inc.php"):
            remote.rename("config_inc.php", "config_inc.php.back")
        remote.upload(os.path.join(os.path.dirname(__file__), "resources/config_inc.php"), "config_inc.php")


def restore_server_configuration(host, username, password):
    with ftputil.FTPHost(host, username, password) as remote:
        if remote.path.isfile("config_inc.php.back"):
            if remote.path.isfile("config_inc.php"):
                remote.remove("config_inc.php")
                remote.rename("config_inc.php.back", "config_inc.php")


# finalization fixture(logout and close browser)
@pytest.fixture(scope="session", autouse=True)  # make all tests in one launch of test and automatic
def stop(request):
    def fin():  # one logout for all tests
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")




