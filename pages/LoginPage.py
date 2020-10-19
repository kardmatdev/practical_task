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

    __FORGOT_PASSWORD_LINK = (By.XPATH, "//*[contains(text(),'Forgot password?')]")

    __RESET_PASSWORD_TEXT = (By.XPATH, "//h1[contains(text(),'Reset your password')]")

    __RESET_PASSWORD_EMAIL_FIELD = (By.NAME, "email")

    __RESET_PASSWORD_BUTTON = (By.XPATH, "//button[contains(text(),'Reset password')]")

    __RESET_PASSWORD_LINK_TEXT_AFTER_RESETTING_PASSWORD = (By.XPATH, "//div[contains(text(),'We sent reset password link to your e-mail.')]")


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

    def click_forgot_password_link(self):
        driver = self.__driver
        forgot_password_link_wait = Helper.wait_for_element_clickable(driver, self.__FORGOT_PASSWORD_LINK)
        forgot_password_link_wait.click()

    def is_reset_password_text_exists(self):
        driver = self.__driver
        return driver.find_element(*self.__RESET_PASSWORD_TEXT).is_displayed()

    def fill_reset_password_email_field_and_click_reset_password_button(self, user_email):
        driver = self.__driver
        driver.find_element(*self.__RESET_PASSWORD_EMAIL_FIELD).send_keys(user_email)
        driver.find_element(*self.__RESET_PASSWORD_BUTTON).click()

    def is_we_sent_reset_password_link_exists(self):
        driver = self.__driver
        reset_password_text_wait = Helper.wait_for_element_clickable(driver, self.__RESET_PASSWORD_LINK_TEXT_AFTER_RESETTING_PASSWORD)
        return driver.find_element(*self.__RESET_PASSWORD_LINK_TEXT_AFTER_RESETTING_PASSWORD).is_displayed()













