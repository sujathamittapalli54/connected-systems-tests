import logging
import os

def get_logger(name="framework"):
    logger = logging.getLogger(name)

    if not logger.handlers:
        logger.setLevel(logging.INFO)

        os.makedirs("logs", exist_ok=True)

        fh = logging.FileHandler("logs/test.log")
        ch = logging.StreamHandler()

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(ch)

    return logger