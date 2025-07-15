import logging
import os
from datetime import datetime

os.makedirs("logs", exist_ok=True)

def get_logger(name="telegram_scraper"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler = logging.FileHandler(f"logs/{name}_{datetime.now().strftime('%Y%m%d')}.log")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
