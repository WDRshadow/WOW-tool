import config
import subprocess
from module import logger


# class for running openFAST
class FAST:
    def __init__(self):
        self.logger = logger.logger
        self.path = config.openFAST_path

    # run openFAST simulation
    def run(self):
        self.logger.info("Running openFAST simulation.")
        try:
            subprocess.check_call([config.openFAST_command, self.path + "/main.fst"])
        except Exception as err:
            self.logger.error("Run openFAST failed.")
            self.logger.error(err)
            exit()
