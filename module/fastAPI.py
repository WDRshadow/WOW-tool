import config


# class for running openFAST
class FAST:
    def __init__(self, logger):
        self.logger = logger
        self.path = config.openFAST_path

    # generate the .gdf file
    def run(self):
        self.logger.info("Running openFAST simulation.")
