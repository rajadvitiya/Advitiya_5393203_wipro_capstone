import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        # Ensure logs directory exists
        log_dir = os.path.join(os.getcwd(), "logs")
        os.makedirs(log_dir, exist_ok=True)

        # Configure logging
        logging.basicConfig(
            filename=os.path.join(log_dir, "automation.log"),
            format="%(asctime)s - %(levelname)s - %(message)s",
            level=logging.INFO
        )
        logger = logging.getLogger()
        return logger