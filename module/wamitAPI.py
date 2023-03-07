import config


# class for running WAMIT
class WAMIT:
    def __init__(self, logger):
        self.logger = logger
        self.path = config.wamit_path

    # generate the .gdf file
    def run(self):
        self.logger.info("Running WAMIT to get the hydrostatic data.")
