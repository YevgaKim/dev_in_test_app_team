from contextlib import nullcontext as does_not_raise
from selenium.common.exceptions import NoSuchElementException
import configparser
import pytest
import time


#Получаю данные(логин, пароль) с файла config.ini
config = configparser.ConfigParser()
config.read("utils/config.ini")

LOGIN = config['USER']['login']
PASSWORD = config['USER']['password']


#Фикстура которая один раз нажимает кнопочку Авторизоваться в первом меню
@pytest.fixture(scope='session')
def click_auth(create_page):
    page = create_page
    page.find_element("com.ajaxsystems:id/authHelloLogin").click()
    return page


#Тестировка авторизации
# 1 - неправильный имейл
# 2 - неверный пароль или имейл
# 3 - всё верно
# P.S. у меня тест построен так что он лишь проверяет зашло или нет поэтому множество 
# вариантов не учитывал, возможно нужно было, но не понимаю зачем
@pytest.mark.parametrize(
        "login, password, expectation", 
        [   ("aaaaaaa","aaaaaaaa", pytest.raises(NoSuchElementException)), 
            ("jekanew09@gmail.com","aaaaaaaa", pytest.raises(NoSuchElementException)),
            (LOGIN, PASSWORD, does_not_raise()),
            
        ]
)
def test_user_login(login,password, expectation, user_login_fixture, create_page, click_auth):
    with expectation:
        # Получаю экземпляр класса LoginPage
        login_page = user_login_fixture
        # Авторизация с помощью метода auth который просто вставляет значения в поля
        login_page.auth(login, password)
        # Нажатие на кнопку "Авторизоваться"
        login_page.but_auth()
        # Ожидание подгрузки
        time.sleep(5)
        
        # Проверяет есть ли элемент на странице, если нет то возникает ошибка
        # "NoSuchElementException", если есть то это главная страница(насколько я понял)
        # и авторизация прошла успешно
        assert login_page.find_element("com.ajaxsystems:id/icNoHub") 
