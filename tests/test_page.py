from framework.page import Page
from contextlib import nullcontext as does_not_raise
from selenium.common.exceptions import NoSuchElementException, InvalidElementStateException
import pytest




# Класс который тестирует все(почти) методы класса Page
class TestPage():
    
    # Тестировка правильно ли сработала фикстура create_page
    def test_create_page(self, create_page):
        page = create_page
        assert isinstance(page, Page)



    # Тестировка поиска элемента по АЙДИ
    # 1 - Проверка на множество элементов(в итоге ошибки нет)
    # 2 - Правильный поиск элемента
    # 3 - Несуществующий элемент
    @pytest.mark.parametrize(
            "id, expectation",
            [
                ("com.ajaxsystems:id/text", does_not_raise()),
                ("com.ajaxsystems:id/authHelloLogin", does_not_raise()),
                ("com.ajaxsystems:id/authHelloLoginADadsf", pytest.raises(NoSuchElementException)),
                
            ]
    )
    def test_find_element(self, id, expectation, create_page):
        with expectation:
            page = create_page
            element = page.find_element(id)
            assert element



    # Тестирования нажатия 
    # Впринципе всё так же как и у find_element, потому что этот метод зависим от того 
    @pytest.mark.parametrize(
            "id, expectation",
            [
                ("com.ajaxsystems:id/build", does_not_raise()),
                ("com.ajaxsystems:id/authHelloLogin", does_not_raise()),
                ("com.ajaxsystems:id/authHelloLoginADadsf", pytest.raises(NoSuchElementException)),
            ]
    )
    def test_click(self, id, expectation, create_page):
        with expectation:
            page = create_page
            element = page.find_element(id).click()
            assert element


    # Тестирование вставки
    # 1 и 2 - всё верно
    # 3 - нет такого элемента
    # 4 - невозможно выполнить действие 
    @pytest.mark.parametrize(
            "id, text, expectation",
            [
                ("com.ajaxsystems:id/authLoginEmail", "dsa", does_not_raise()),
                ("com.ajaxsystems:id/authLoginPassword", "dsa", does_not_raise()),
                ("com.ajaxsystems:id/authLoginPasswordddd", "dsa", pytest.raises(NoSuchElementException)),
                ("com.ajaxsystems:id/compose_view","dsad", pytest.raises(InvalidElementStateException))
     
            ]
    )
    def test_paste(self, id, text, expectation, create_page):
        with expectation:
            page = create_page
            element = page.find_element(id).paste(text)
            assert element





        

