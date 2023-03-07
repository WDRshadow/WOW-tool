import config
import subprocess


# class for running WAMIT
class WAMIT:
    def __init__(self, logger):
        self.logger = logger
        self.path = config.wamit_path

    # calculate the hydrostatic data
    def run(self):
        self.logger.info("Running WAMIT to get the hydrostatic data.")
        try:
            subprocess.run(self.path + "/WAMIT.exe")
        except Exception as err:
            self.logger.warn("Run WAMIT failed.")
            self.logger.error(err)
