import config
from module import logger
from module.fileAPI import FileAPI
import matlab.engine


# class for running MATLAB
class MATLAB:
    def __init__(self):
        self.logger = logger.logger
        self.path = config.matlab_path

    # update the variables
    def update(self, column_radius, hp_radius, draft, column_distance):
        FileAPI(self.path, "gdf_script.m").changer() \
            .change(6, str(column_radius), 3) \
            .change(7, str(hp_radius), 3) \
            .change(10, str(draft), 3) \
            .change(8, str(column_distance), 3) \
            .do()
        return self

    # generate the .gdf file
    def run(self):
        self.logger.info("Running MATLAB to generate .gdf file.")
        try:
            eng = matlab.engine.start_matlab()
            eng.cd(self.path)
            eng.gdf_script(nargout=0)
            FileAPI(self.path, "wow.gdf").move(config.temp_path)
            FileAPI(self.path, "wow.cfg").move(config.temp_path)
        except Exception as err:
            self.logger.error("Run MATLAB failed.")
            self.logger.error(err)
            exit()
