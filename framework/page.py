from appium.webdriver.common.mobileby import MobileBy
import time

#Декоратор для избежания повторения кода 
def handle_no_element(func):
    def wrapper(self, *args, **kwargs):
        if self.element:
            return func(self, *args, **kwargs)
        else:
            raise ValueError(f"No element found to use.")
    return wrapper



class Page:

    def __init__(self, driver):
        self.driver = driver
        self.element = None


    # Поиск элемента по АЙДИ, потому что он более менее уникален в отличии от классов
    def find_element(self, id : str):
        self.element = self.driver.find_element(by=MobileBy.ID, value=id)
        if isinstance(self.element, list):
            raise ValueError
        return self
    
    # Так же как и в методе find_element поиск по АЙДИ
    def find_elements(self, id : str):
        self.elements = self.driver.find_elements(by=MobileBy.ID, value=id)
        return self.elements
        

    @handle_no_element
    def click(self):   
        self.element.click()
        time.sleep(2)
        return self

    @handle_no_element
    def paste(self, text:str):
        self.element.send_keys(text)
        time.sleep(1)
        return self

    @handle_no_element
    def clear(self):
        self.element.clear()
        time.sleep(1)
        return self
    
    #Получаю страничку в html вид(нужно было на этапе построения)
    @property
    def get_page_source(self) -> str:
        return self.driver.page_source

