

class DashboardPage:

    __URL = "https://manager.greensteam.com/dashboard"

    def __init__(self, driver):
        self.__driver = driver


    def is_logged_successfully(self):
        driver = self.__driver
        return driver.current_url == self.__URL


