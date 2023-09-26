import logging
from logging.handlers import TimedRotatingFileHandler

logging.basicConfig(level=logging.INFO)

handler = TimedRotatingFileHandler(
    "daily_log.log", when="midnight", interval=1, backupCount=7, encoding="utf-8"
)

logger = logging.getLogger()
logger.addHandler(handler)

logger.info("У попа була собака він її любив")
logger.error("Вона зїла кусок мяса він її убив")
