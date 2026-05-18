import os
import time
from selenium.webdriver.remote.webdriver import WebDriver


class ScreenshotUtil:
    @staticmethod
    def capture(driver: WebDriver, name: str = "screenshot"):
        """
        Capture a screenshot and save it under /screenshots folder.

        :param driver: Selenium WebDriver instance
        :param name: Base name for the screenshot file
        :return: Absolute path of the saved screenshot
        """
        # Ensure screenshots directory exists
        screenshot_dir = os.path.join(os.getcwd(), "screenshots")
        os.makedirs(screenshot_dir, exist_ok=True)

        # Timestamp for uniqueness
        timestamp = time.strftime("%Y%m%d_%H%M%S")

        # File path
        file_path = os.path.join(screenshot_dir, f"{name}_{timestamp}.png")

        # Capture screenshot
        driver.save_screenshot(file_path)

        return file_path