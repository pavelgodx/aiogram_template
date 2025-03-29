import logging
import sys
from pathlib import Path
from logging.handlers import RotatingFileHandler


class LoggerFactory:
    LOG_DIR = Path(__file__).resolve().parent / "logs"
    LOG_FORMAT = "[%(asctime)s] [%(levelname)s] [%(name)s] — %(message)s"

    def __init__(self, level=logging.DEBUG):
        self.level = level
        self.LOG_DIR.mkdir(exist_ok=True)

    def get_logger(self, name: str) -> logging.Logger:
        logger = logging.getLogger(name)
        logger.setLevel(self.level)

        if not logger.handlers:
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setFormatter(logging.Formatter(self.LOG_FORMAT))
            logger.addHandler(console_handler)

            filename = name.replace(".", "_") + ".log"
            file_path = self.LOG_DIR / filename

            file_handler = RotatingFileHandler(
                file_path,
                maxBytes=5 * 1024 * 1024,
                backupCount=5,
                encoding="utf-8"
            )
            file_handler.setFormatter(logging.Formatter(self.LOG_FORMAT))
            logger.addHandler(file_handler)

        return logger
