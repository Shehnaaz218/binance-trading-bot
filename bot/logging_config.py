import logging

def setup_logger():
    logger = logging.getLogger("trading_bot")

    # Prevent duplicate handlers
    if not logger.handlers:
        logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler("bot.log")
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger