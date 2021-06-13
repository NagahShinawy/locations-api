"""
created by Nagaj at 13/06/2021
"""
import logging
from logging import handlers

logger = logging.getLogger("")
logger.setLevel(logging.INFO)
format_ = logging.Formatter(
    "%(asctime)s || %(process)d || %(processName)s || %(module)s || %(funcName)s ||"
    " %(lineno)d || %(name)s || %(levelname)s  ||  %(levelno)s || %(message)s || %(msecs)s seconds",
    datefmt="%d-%b-%y %H:%M:%S",
)

ch = logging.StreamHandler()
ch.setFormatter(format_)
logger.addHandler(ch)

fh = handlers.RotatingFileHandler("logs.log", maxBytes=(1048576 * 5), backupCount=7)
fh.setFormatter(format_)
logger.addHandler(fh)
