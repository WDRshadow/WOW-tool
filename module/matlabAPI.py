import config
import matlab.engine


# class for running MATLAB
class MATLAB:
    def __init__(self, logger):
        self.logger = logger
        self.path = config.matlab_path

    # generate the .gdf file
    def run(self):
        self.logger.info("Running MATLAB to generate .gdf file.")
        try:
            eng = matlab.engine.start_matlab()
            eng.cd(self.path)
            eng.gdf_script(nargout=0)
        except Exception as err:
            self.logger.warn("Run MATLAB failed.")
            self.logger.error(err)
