import sys
import config
import logging
from module import matlabAPI, wamitAPI, fastAPI, mdaoInterface

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


def main_loop(times):
    for i in range(times):
        logger.info("Running simulation and optimization in " + str(i + 1) + " times.")
        matlabAPI.MATLAB(logger).run()
        wamitAPI.WAMIT(logger).run()
        fastAPI.FAST(logger).run()
        mdaoInterface.MDAO(logger).run()


command = str(sys.argv[1])

if command == "run":
    main_loop(config.loop_times)
elif command == "openfast":
    fastAPI.FAST(logger).run()
elif command == "matlab":
    matlabAPI.MATLAB(logger).run()
elif command == "wamit":
    wamitAPI.WAMIT(logger).run()
elif command == "openmdao":
    mdaoInterface.MDAO(logger).run()
else:
    logger.error("No command name " + command)
