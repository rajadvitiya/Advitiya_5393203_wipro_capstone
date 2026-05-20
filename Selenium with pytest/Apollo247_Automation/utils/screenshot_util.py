import os
import time
from selenium.webdriver.remote.webdriver import WebDriver


class ScreenshotUtil:

    @staticmethod
    def capture(
            driver: WebDriver,
            test_name: str,
            status: str
    ):

        screenshot_dir = os.path.join(
            os.getcwd(),
            "screenshots"
        )

        os.makedirs(
            screenshot_dir,
            exist_ok=True
        )

        timestamp = time.strftime(
            "%Y%m%d_%H%M%S"
        )

        clean_test_name = (
            test_name
            .replace("/", "_")
            .replace("\\", "_")
            .replace(":", "_")
            .replace(" ", "_")
        )

        file_name = (
            f"{clean_test_name}"
            f"_{status}"
            f"_{timestamp}.png"
        )

        file_path = os.path.join(
            screenshot_dir,
            file_name
        )

        driver.save_screenshot(file_path)

        return file_path