import pytest
from selenium import webdriver
from Apps.app import Application


@pytest.fixture()  # Запуск Google Chrome
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


# @pytest.fixture()                            # Запуск FireFoxe
# def driver(request):
#     wd = webdriver.Firefox(firefox_binary='C:\\Program Files\\Mozilla Firefox\\firefox.exe')
#     request.addfinalizer(wd.quit)
#     return wd


# @pytest.fixture()  # Запуск Edge
# def driver(request):
#     wd = webdriver.Edge("C:\\Tools\\msedgedriver.exe")
#     request.addfinalizer(wd.quit)
#     return wd


@pytest.fixture
def app(request):
    app = Application()
    request.addfinalizer(app.quit)
    return app
