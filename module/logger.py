import logging


# Generate the logger
logger = logging.getLogger('WOW-tool')
logger.setLevel(logging.INFO)
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.INFO)
fileHandler = logging.FileHandler('logs/wow.log', mode='a', encoding='UTF-8')
fileHandler.setLevel(logging.NOTSET)
formatter = logging.Formatter('[%(name)s] [%(asctime)s] [%(levelname)s]: %(message)s')
consoleHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)
logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)
