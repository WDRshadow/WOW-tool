import config
import os
from module import logger
from module.fileAPI import FileAPI
from module import matlabAPI, wamitAPI, fastAPI, mdaoInterface


# main loop for simulation-optimization
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
            # MATLAB progress ------------------------------------------------------------------------------------------
            matlab = matlabAPI.MATLAB()
            FileAPI(matlab.path, "gdf_script.m").changer() \
                .change(6, str(self.column_radius), 3) \
                .change(7, str(self.hp_radius), 3) \
                .change(10, str(self.draft), 3) \
                .change(8, str(self.column_distance), 3) \
                .do()
            matlab.run()
            # WAMIT progress -------------------------------------------------------------------------------------------
            FileAPI(matlab.path, "wow.gdf").move(config.temp_path).copy(config.wamit_path)
            wamit = wamitAPI.WAMIT()
            '''input file update ...'''
            wamit.check().run()
            # openFAST progress ----------------------------------------------------------------------------------------
            if not os.path.exists(os.path.join(config.openFAST_path, "HydroData")):
                os.makedirs(os.path.join(config.openFAST_path, "HydroData"))
            FileAPI(wamit.path, "wow.1").move(config.temp_path).copy(os.path.join(config.openFAST_path, "HydroData"))
            FileAPI(wamit.path, "wow.3").move(config.temp_path).copy(os.path.join(config.openFAST_path, "HydroData"))
            FileAPI(wamit.path, "wow.hst").move(config.temp_path).copy(os.path.join(config.openFAST_path, "HydroData"))
            openfast = fastAPI.FAST()
            '''input file update ...'''
            openfast.run()
            # openMDAO progress ----------------------------------------------------------------------------------------
            self.update(mdaoInterface.MDAO().run().result())
