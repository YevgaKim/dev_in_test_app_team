
### P.S Не знаю правильно ли выполнил, но сделал как сам считал нужным
### ЛОГИ ДЛЯ ПРОВЕРКИ
1 - pytest tests/test_page.py::TestPage -v -s -p no:warnings - тест базовых действий 
2 - pytest tests/login/test_login.py::test_user_login -v -s -p no:warnings - тест авторизации
3 - pytest tests/SideBar/test_sidebar.py -v -s -p no:warnings - тест SideBar


### Ajax Systems, Python developer in test for Application team
Для выполнения тестового задания Вам нужно установить приложение Ajax Systems на телефон (если у вас нет реального андроид устройства то вы можете использовать эмулятор).

### Задание
1) Написать базовый функционал для работы с приложением (поиск элемента, клик элемента и тд).
2) Написать тест логина пользователя в приложение (позитивный и негативные кейсы).
3) Использовать параметризацию.
4) Закомитить выполненное задание на гитхаб.

### Дополнительное задание (опционально)
1) *Реализовать логирование теста.
2) *Реализовать динамическое определение udid телефона через subprocess
3) **Написать на проверку элементов SideBar (выезжающее меню слева).

### Полезные ссылки
1) Приложение - https://play.google.com/store/apps/details?id=com.ajaxsystems
2) Работа с реальным телефоном - https://developer.android.com/studio/command-line/adb
3) Настройка эмулятора - https://developer.android.com/studio/run/emulator
4) Настройка аппиума - https://appium.io/docs/en/2.0/quickstart/
5) Инспектор приложения - https://appium.io/docs/en/2.0/quickstart/uiauto2-driver/

### Login credentials
login - qa.ajax.app.automation@gmail.com
password - qa_automation_password
