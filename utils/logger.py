import logging
import os


def setup_logger(name, info_log_file, error_log_file, level=logging.INFO):
    # Create a directory for log files if it doesn't exist
    log_dir = os.path.dirname(info_log_file)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Define formatters
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

    # Create file handlers for info and error logs
    info_handler = logging.FileHandler(info_log_file)
    info_handler.setLevel(logging.INFO)
    info_handler.setFormatter(formatter)

    error_handler = logging.FileHandler(error_log_file)
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)

    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # Create a logger and set its level
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # Capture all levels of logs
    logger.addHandler(info_handler)
    logger.addHandler(error_handler)
    logger.addHandler(console_handler)

    return logger


# Setup logger with separate files for info and error logs
logger = setup_logger(
    'github_logger',
    'logs/github_info.log',
    'logs/github_error.log'
)


# Example usage
logger.info('This is an info message.')
logger.error('This is an error message.')