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

    # update the conditions for next simulation
    def update(self, result):
        pass

    def run(self):
        for i in range(self.times):
            self.logger.info("Running simulation and optimization in " + str(i + 1) + " times.")
            # MATLAB progress ------------------------------------------------
            matlab = matlabAPI.MATLAB()
            FileAPI(matlab.path, "gdf_script.m").changer()\
                .change(6, str(self.column_radius), 3)\
                .change(7, str(self.hp_radius), 3)\
                .change(8, str(self.draft), 3)\
                .change(9, str(self.column_distance), 3)\
                .do()
            matlab.run()
            FileAPI(matlab.path, "wow.gdf").copy(config.temp_path).copy(config.wamit_path)
            # WAMIT progress -------------------------------------------------
            wamit = wamitAPI.WAMIT()
            # file update ...
            wamit.run()
            # openFAST progress ----------------------------------------------
            openfast = fastAPI.FAST()
            # file update ...
            openfast.run()
            # openMDAO progress ----------------------------------------------
            self.update(mdaoInterface.MDAO().run().result())
