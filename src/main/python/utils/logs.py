import logging

from src.main.python.utils.path import get_project_root

root = get_project_root()

formatter = logging.Formatter('%(asctime)s \t %(levelname)s \t %(message)s')


def to_log_error(log_text):
    logger = logging.getLogger('application_error_log')
    file_handler = logging.FileHandler(str(root) + '/logs/error.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.ERROR)

    logger.error(log_text)


def to_log_debug(log_text):
    logger = logging.getLogger('application_debug_log')
    file_handler = logging.FileHandler(str(root) + '/logs/debug.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)

    logger.debug(log_text)


def to_log_fatal(log_text):
    logger = logging.getLogger('application_fatal_log')
    file_handler = logging.FileHandler(str(root) + '/logs/fatal.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.FATAL)

    logger.fatal(log_text)


def to_log_warning(log_text):
    logger = logging.getLogger('application_warning_log')
    file_handler = logging.FileHandler(str(root) + '/logs/warning.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.WARNING)

    logger.warning(log_text)


def to_log_info(log_text):
    logger = logging.getLogger('application_info_log')
    file_handler = logging.FileHandler(str(root) + '/logs/info.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)

    logger.warning(log_text)
