
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as WWait


class Helper:

    @classmethod
    def wait_for_element_clickable(cls, driver, element_locator):
        webdriver_wait = WWait(driver, 10)
        return webdriver_wait.until(EC.element_to_be_clickable(element_locator))

    @classmethod
    def wait_for_element_selected(cls, driver, element_locator):
        webdriver_wait = WWait(driver, 10)
        return webdriver_wait.until(EC.element_to_be_selected(element_locator))
