import subprocess
import re

def get_connected_devices():
    try:
        # Выполняем команду adb для получения списка подключенных устройств
        result = subprocess.run(["E:\\Android\\platform-tools\\adb", "devices"], capture_output=True, text=True, check=True)
        output = result.stdout
        
        # Извлекаем строки с устройствами из вывода
        devices = re.findall(r"(\S+)\s+device\b", output)
        return devices
    except subprocess.CalledProcessError as e:
        print("Ошибка при выполнении команды adb:", e)
        return []

def get_udid():
    devices = get_connected_devices()
    if devices:
        # Берем первое подключенное устройство
        return devices[0]
    else:
        print("Нет подключенных устройств")
        return None


def android_get_desired_capabilities():
    return {
        "autoGrantPermissions": True,
        "automationName": "uiautomator2",
        "newCommandTimeout": 500,
        "noSign": True,
        "platformName": "Android",
        "platformVersion": "11",
        "resetKeyboard": True,
        "systemPort": 8301,
        "takesScreenshot": True,
        "udid": get_udid(),
        "appPackage": "com.ajaxsystems",
        "appActivity": "com.ajaxsystems.ui.activity.LauncherActivity"
}
