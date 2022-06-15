import logging

def criticalLog(msg):
    logging.basicConfig(
        level=logging.CRITICAL,
        format="{asctime} {levelname} {message}",
        style='{',
        filename="logs/dev.log",
        filemode="a"
    )
    logging.critical(msg)


def errorLog(msg):
    logging.basicConfig(
        level=logging.ERROR,
        format="{asctime} {levelname} {message}",
        style='{',
        filename="logs/dev.log",
        filemode="a"
    )
    logging.error(msg)


def warningLog(msg):
    logging.basicConfig(
        level=logging.WARNING,
        format="{asctime} {levelname} {message}",
        style='{',
        filename="logs/dev.log",
        filemode="a"
    )
    logging.warning(msg)


def infoLog(msg):
    logging.basicConfig(
        level=logging.INFO,
        format="{asctime} {levelname} {message}",
        style='{',
        filename="logs/dev.log",
        filemode="a"
    )
    logging.info(msg)


def debugLog(msg):
    logging.basicConfig(
        level=logging.DEBUG,
        format="{asctime} {levelname} {message}",
        style='{',
        filename="logs/dev.log",
        filemode="a"
    )
    logging.debug(msg)