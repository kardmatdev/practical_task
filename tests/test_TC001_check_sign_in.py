import os

import pytest
import logging

from utils.DriverFactory import DriverFactory
from pages.LoginPage import LoginPage
from pages.DashboardPage import DashboardPage

logger = logging.getLogger("TC001_logger")


@pytest.fixture()
def driver():
    browser = os.environ["BROWSER_NAME"]
    # browser = "Chrome"
    logger.info(f"Browser is {browser}")
    driver = DriverFactory.get_instance(browser)

    yield driver

    DriverFactory.close_driver()

@pytest.mark.Login
def test_check_sign_in_with_valid_credentials(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.fill_the_sign_in_form_and_login("john@example.com", "test")
    dashboards_page = DashboardPage(driver)
    assert dashboards_page.is_logged_successfully()

@pytest.mark.Login
def test_check_sign_in_with_invalid_credentials(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.fill_the_sign_in_form_and_login("invalid_email@example.com", "invalid_password")
    assert login_page.is_invalid_creds_text_exists()

@pytest.mark.Password
def test_forgot_password_link_check(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.click_forgot_password_link()
    assert login_page.is_reset_password_text_exists()

@pytest.mark.Password
def test_reset_password_check(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.click_forgot_password_link()
    assert login_page.is_reset_password_text_exists()
    login_page.fill_reset_password_email_field_and_click_reset_password_button("john@example.com")
    assert login_page.is_we_sent_reset_password_link_exists()



