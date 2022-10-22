import logging
import os

logfile = "/home/{}/lsu/logs/dev.log".format(os.getlogin())


def criticalLog(msg):
    logging.basicConfig(
        level=logging.CRITICAL,
        format="{name} {name} {asctime} {levelname} {message} {exc_info}",
        style='{',
        filename=logfile,
        filemode="a"
    )
    logging.critical(msg)


def errorLog(msg):
    logging.basicConfig(
        level=logging.ERROR,
        format="{name} {asctime} {levelname} {message} {exc_info}",
        style='{',
        filename=logfile,
        filemode="a"
    )
    logging.error(msg)


def warningLog(msg):
    logging.basicConfig(
        level=logging.WARNING,
        format="{name} {asctime} {levelname} {message} {exc_info}",
        style='{',
        filename=logfile,
        filemode="a"
    )
    logging.warning(msg)


def infoLog(msg):
    logging.basicConfig(
        level=logging.INFO,
        format="{name} {asctime} {levelname} {message} {exc_info}",
        style='{',
        filename=logfile,
        filemode="a"
    )
    logging.info(msg)


def debugLog(msg):
    logging.basicConfig(
        level=logging.DEBUG,
        format="{name} {asctime} {levelname} {message} {exc_info}",
        style='{',
        filename=logfile,
        filemode="a"
    )
    logging.debug(msg)
