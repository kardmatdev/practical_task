import logging

from selenium.webdriver.common.by import By

from utils.Helper import Helper


class LoginPage:

    __log = logging.getLogger("LoginPageLogger")

    __URL = "https://manager.greensteam.com"

    __EMAIL_FIELD = (By.NAME, "username")

    __PASSWORD_FIELD = (By.NAME, "password")

    __SIGN_IN_BUTTON = (By.XPATH, "//button[contains(text(),'Sign in')]")

    __INVALID_CREDS_TEXT = (By.XPATH, "//div[contains(text(),'Invalid username/password.')]")


    def __init__(self, driver):
        self.__driver = driver

    def load(self):
        self.__log.info("Opening LoginPage")
        self.__driver.get(self.__URL)


    def fill_the_sign_in_form_and_login(self, username, password):
        driver = self.__driver
        self.__log.info("Waiting for login page")
        email_field_wait = Helper.wait_for_element_clickable(driver, self.__EMAIL_FIELD)
        email_field_wait.click()
        self.__log.info("Filling username")
        driver.find_element(*self.__EMAIL_FIELD).send_keys(username)
        self.__log.info("Filling password")
        driver.find_element(*self.__PASSWORD_FIELD).send_keys(password)
        self.__log.info("Clicking sign in button")
        driver.find_element(*self.__SIGN_IN_BUTTON).click()


    def is_invalid_creds_text_exists(self):
        driver = self.__driver
        return driver.find_element(*self.__INVALID_CREDS_TEXT).is_displayed()







