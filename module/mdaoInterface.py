from interface.interface import OpenMDAO
from interface.optimization import FWOptimise
from module import logger


# class for running openMDAO
class MDAO:
    def __init__(self):
        self.logger = logger.logger
        self.openMDAO = FWOptimise()  # a instance of openMDAO
        self.simulation_data = self.read_fast()  # simulation output data

    # function to read FAST output files
    def read_fast(self):
        pass

    # update new parameters to the main loop
    def result(self):
        pass

    # run openMDAO
    def run(self):
        self.logger.info("Running openMDAO optimisation.")
        self.openMDAO.run(self.simulation_data)
        return self
