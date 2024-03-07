from selenium.common.exceptions import NoSuchElementException
import pytest
import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



# Автоматический скрипт для авторизации и открытия SideBar
def test_sidebar(auth_to_sidebar):
    page = auth_to_sidebar
    element = page.find_element("com.ajaxsystems:id/menuDrawer").click()
    assert element

# Проверка текста элементов SideBar
def test_text(get_elements_of_sidebar):
    elements = get_elements_of_sidebar

    assert elements[0].text == "Настройки приложения"
    assert elements[1].text == "Помощь"
    assert elements[2].text == "Сообщить о проблеме"
    assert elements[3].text == "Видеонаблюдение"


# Фикстура которая сокращает повторения кода для функций 
# test_settings, test_help, test_video 
@pytest.fixture
def check_sidebar_element(get_elements_of_sidebar, create_page):
    def _check_sidebar_element(index, expected_element_id):
        # Получает все(почти) элементы SideBar
        elements = get_elements_of_sidebar
        # нажимает на нужный элемент
        elements[index].click()
        time.sleep(2)
        page = create_page
        # Находит уникальный элемент на странице на которую перешел
        attend = page.find_element(expected_element_id)
        # Нажимает кнопку назад
        page.find_element("com.ajaxsystems:id/back").click()
        time.sleep(1)
        # Открывает SideBar
        page.find_element("com.ajaxsystems:id/menuDrawer").click()
        time.sleep(1)
        return attend
    return _check_sidebar_element


# Проверяет элемент "Настройки приложения" на кликабельность и переход дальше
def test_settings(check_sidebar_element):
    attend = check_sidebar_element(0, "com.ajaxsystems:id/plugImage")
    assert attend

# Проверяет элемент "Помощь" на кликабельность и переход дальше
def test_help(check_sidebar_element):
    attend = check_sidebar_element(1, "com.ajaxsystems:id/navigation")
    assert attend

# Проверяет элемент "Видеонаблюдение" на кликабельность и переход дальше
def test_video(check_sidebar_element):
    attend = check_sidebar_element(3, "com.ajaxsystems:id/hikvision")
    assert attend

# Проверяет элемент "+ Добавить хаб" на кликабельность и переход дальше
def test_hub(create_page):
    page = create_page
    # Нажимает на элемент "+ Добавить хаб"
    page.find_element("com.ajaxsystems:id/addHub").click()
    time.sleep(2)

    # Находит уникальный элемент на странице на которую перешли
    attend = page.find_element("com.ajaxsystems:id/hubAddManuallyButton")

    # Находит и нажимает кнопку "Назад"
    page.find_element("com.ajaxsystems:id/backButton").click()

    time.sleep(1)
    # Повторно открывает SideBar
    page.find_element("com.ajaxsystems:id/menuDrawer").click()
    time.sleep(1)
    assert attend


# Проверяет элемент "Сообщить о проблеме" на кликабельность и переход дальше
def test_report(get_elements_of_sidebar, create_page):
    # Получает элементы SideBar
    elements= get_elements_of_sidebar
    # Нажимает конкретно на "Сообщить о проблеме"
    # P.S. не запихнул под одну фикстуру с другими, потому что кнопка выхода не такая
    elements[2].click()
    time.sleep(3)
    page = create_page
    # Находит уникальный элемент тем самым понимая что на той странице на которой должны быть 
    attend = page.find_element("com.ajaxsystems:id/touch_outside")
    assert attend

    






