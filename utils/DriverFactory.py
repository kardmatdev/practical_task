import sys

from selenium.webdriver import Chrome
from selenium.webdriver import Firefox


class DriverFactory:

    __instance = None

    @classmethod
    def get_instance(cls, browser):
        if cls.__instance is None and browser == "Chrome":
            # chromedriver = "drivers/chromedriver.exe"
            __instance = Chrome()
            __instance.maximize_window()
            return __instance
        elif cls.__instance is None and browser == "Firefox":
            # geckodriver = "drivers/geckodriver.exe"
            __instance = Firefox()
            __instance.maximize_window()
            return __instance
        else:
            print("No browser selected")
            sys.exit(1)


    @classmethod
    def close_driver(cls):
        if cls.__instance is not None:
            cls.__instance.close()
            cls.__instance = None


