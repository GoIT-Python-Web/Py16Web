import logging

log_format = "[%(levelname)s] %(asctime)s: %(name)s %(module)s %(funcName)s:%(lineno)d - %(message)s"

file_handler = logging.FileHandler("application.log")
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(logging.Formatter(log_format))

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(logging.Formatter(log_format))


def get_logger(name, level):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    return logger


logger = get_logger('my_logger', logging.DEBUG)