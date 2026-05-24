from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def click(self, locator):

        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            element
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    def send_keys(self, locator, text):

        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        element.clear()
        element.send_keys(text)

    def wait_until_clickable(self, locator, timeout=20):

        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_until_visible(self, locator, timeout=20):

        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def is_displayed(self, locator):

        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).is_displayed()