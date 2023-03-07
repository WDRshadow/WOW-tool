from module import logger
from module.fileAPI import FileAPI
import config


# class for running openMDAO
class MDAO:
    def __init__(self):
        self.logger = logger.logger
        # self.openMDAO = OpenMDAO()  # a instance of openMDAO
        # self.simulation_data = self.read_fast()  # simulation output data

    # function to read FAST output files
    def read_fast(self):
        pass

    # update new parameters to the main loop
    def update(self, main):
        # main.variable = openMDAO.variable
        # ...
        pass

    # run openMDAO
    def run(self):
        self.logger.info("Running openMDAO optimisation.")
        # self.openMDAO.someFunctions(self.simulation_data)
        return self
