import config
import subprocess
from module import logger


# class for running WAMIT
class WAMIT:
    def __init__(self):
        self.logger = logger.logger
        self.path = config.wamit_path

    # calculate the hydrostatic data
    def run(self):
        self.logger.info("Running WAMIT to get the hydrostatic data.")
        try:
            subprocess.check_call(config.wamit_command)
        except Exception as err:
            self.logger.error("Run WAMIT failed.")
            self.logger.error(err)
            exit()
