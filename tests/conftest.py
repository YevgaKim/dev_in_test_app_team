from appium import webdriver
from framework.page import Page
from framework.login_page import LoginPage
from utils.android_utils import android_get_desired_capabilities
import subprocess
import time
import pytest
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#Запуск appium
@pytest.fixture(scope='session')
def run_appium_server():
    logger.info("Запуск Appium")
    appium = subprocess.Popen(
        ['appium', '-a', '0.0.0.0', '-p', '4723', '--allow-insecure', 'adb_shell'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True
    )
    time.sleep(3)
    yield
    logger.info("Выключение Appium")
    appium.terminate()
    appium.wait()

#Запуск скрипта 
@pytest.fixture(scope='session')
def driver(run_appium_server):
    logger.info("Запуск драйвера")
    driver = webdriver.Remote('http://localhost:4723', android_get_desired_capabilities())
    time.sleep(4)
    yield driver
    logger.info("Выключение драйвера")


#Получение странички 
@pytest.fixture(scope="session")
def create_page(driver):
    logger.info("Создание странички")
    yield Page(driver)
    logger.info("Удалиние странички")
    

#Создания LoginPage
@pytest.fixture(scope='session')
def user_login_fixture(driver):
    logger.info("Создание странички авторизации")
    yield LoginPage(driver)
    logger.info("Удаление странички авторизации")
    
