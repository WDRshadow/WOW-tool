import config
import subprocess


# class for running openFAST
class FAST:
    def __init__(self, logger):
        self.logger = logger
        self.path = config.openFAST_path

    # run openFAST simulation
    def run(self):
        self.logger.info("Running openFAST simulation.")
        try:
            subprocess.run("openfast " + self.path + "/main.fst")
        except Exception as err:
            self.logger.warn("Run openFAST failed.")
            self.logger.error(err)
