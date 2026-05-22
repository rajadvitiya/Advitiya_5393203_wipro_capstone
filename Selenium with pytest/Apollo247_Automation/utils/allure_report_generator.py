import os
import subprocess

from utils.logger import LogGen

logger = LogGen.loggen()


class AllureReportGenerator:

    @staticmethod
    def generate_report():

        try:

            logger.info(
                "Starting Allure Report Generation"
            )

            project_root = os.getcwd()

            allure_results_dir = os.path.join(
                project_root,
                "reports",
                "allure-results"
            )

            allure_report_dir = os.path.join(
                project_root,
                "reports",
                "allure-report"
            )

            os.makedirs(
                allure_results_dir,
                exist_ok=True
            )

            os.makedirs(
                allure_report_dir,
                exist_ok=True
            )

            if not os.listdir(allure_results_dir):

                logger.error(
                    "Allure Results Directory Is Empty"
                )

                return

            command = (
                f'allure generate "{allure_results_dir}" '
                f'-o "{allure_report_dir}" --clean'
            )

            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True
            )

            if result.returncode == 0:

                logger.info(
                    "Allure Report Generated Successfully"
                )

                logger.info(
                    f"Report Path: {allure_report_dir}"
                )

            else:

                logger.error(
                    "Failed To Generate Allure Report"
                )

                logger.error(result.stderr)

        except Exception as e:

            logger.error(
                "Exception During Allure Report Generation"
            )

            logger.error(str(e))