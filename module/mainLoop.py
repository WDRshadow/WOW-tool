import config
from module import matlabAPI, wamitAPI, fastAPI, mdaoInterface, logger


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
            matlabAPI.MATLAB().update(self.column_radius, self.hp_radius, self.draft, self.column_distance).run()
            wamitAPI.WAMIT().update().check().run()
            fastAPI.FAST().update().run()
            self.update(mdaoInterface.MDAO().run().result())
