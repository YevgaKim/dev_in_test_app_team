import pytest
import configparser
import time

#Получаю данные(логин, пароль) с файла config.ini
config = configparser.ConfigParser()
config.read("utils/config.ini")

LOGIN = config['USER']['login']
PASSWORD = config['USER']['password']

# Фикстура реализовавыет проход скрипта от начальной страницы до входа в акк
@pytest.fixture(scope="session")
def auth_to_sidebar(create_page, user_login_fixture):
    page = create_page

    # Кликает на "Авторизоваться" на начальной странице
    page.find_element("com.ajaxsystems:id/authHelloLogin").click()

    # Создает страницу логина
    login_page = user_login_fixture

    # Авторизуется на странице логина
    login_page.auth(LOGIN, PASSWORD)

    # Нажимает на кнопку "Авторизоваться" после заполнения формы
    login_page.but_auth()
    time.sleep(7)
    yield login_page

# Фикстура находит и сохраняет все элементы SideBar
@pytest.fixture(scope="function")
def get_elements_of_sidebar(create_page):
    page = create_page
    # Находит и отдает элементы SideBar
    elements = page.find_elements("com.ajaxsystems:id/title")
    yield elements