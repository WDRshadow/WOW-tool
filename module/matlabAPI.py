import config


# class for running MATLAB
class MATLAB:
    def __init__(self, logger):
        self.logger = logger
        self.path = config.matlab_path
        self.script = open(self.path+"/gdf_script.m")

    # generate the .gdf file
    def run(self):
        self.logger.info("Running MATLAB to generate .gdf file.")

