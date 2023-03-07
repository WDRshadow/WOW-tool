import config
from module import logger
from module.fileAPI import FileAPI


# main loop for simulation-optimization
from module import matlabAPI, wamitAPI, fastAPI, mdaoInterface


class Main:
    def __init__(self):
        self.logger = logger.logger
        self.times = config.loop_times
        # load initial conditions
        self.column_radius = config.column_radius
        self.column_height = config.column_height
        self.column_mass = config.column_mass
        self.column_distance = config.column_distance
        self.tower_height = config.tower_height
        self.draft = config.draft
        self.hp_radius = config.hp_radius

    def run(self):
        for i in range(self.times):
            self.logger.info("Running simulation and optimization in " + str(i + 1) + " times.")
            # MATLAB progress ------------------------------------------------
            matlab = matlabAPI.MATLAB()
            file = FileAPI(matlab.path + "/gdf_script.m")
            file.change(6, "r", self.column_radius)
            file.change(7, "rH", self.hp_radius)
            file.change(8, "d", self.draft)
            file.change(9, "distance_column", self.column_distance)
            matlab.run()
            # WAMIT progress -------------------------------------------------
            wamit = wamitAPI.WAMIT()
            # file update ...
            wamit.run()
            # openFAST progress ----------------------------------------------
            openfast = fastAPI.FAST()
            # file update ...
            openfast.run()
            # openMDAO progress ----------------------------------------------
            mdaoInterface.MDAO().run().update(self)

