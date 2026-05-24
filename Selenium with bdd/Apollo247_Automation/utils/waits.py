# utils/waits.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WaitUtils:

    def __init__(self, driver, timeout=30):

        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def visible(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def clickable(self, locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )

    def present(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def presence_all(self, locator):
        return self.wait.until(
            EC.presence_of_all_elements_located(locator)
        )

    def invisible(self, locator):
        return self.wait.until(
            EC.invisibility_of_element_located(locator)
        )