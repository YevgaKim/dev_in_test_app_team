from .page import Page




class LoginPage(Page):
    #Функция вставляет логин и пароль в форму, предводительно очищает поле
    def auth(self, login:str, password:str):
        self.find_element("com.ajaxsystems:id/authLoginEmail").clear().paste(login)
        self.find_element("com.ajaxsystems:id/authLoginPassword").clear().paste(password)

    #Функция нажимает на кнопку "Авторизироваться" после того как все поля заполнены 
    def but_auth(self):
        elements = self.find_elements("com.ajaxsystems:id/text")
        elements[1].click()
    
