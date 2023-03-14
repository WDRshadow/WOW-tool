from interface.optimization import FWOptimise
from module import logger


# class for running openMDAO
class MDAO:
    def __init__(self):
        self.logger = logger.logger
        self.openMDAO = FWOptimise()  # a instance of openMDAO
        self.inputs = {}
        self.simulation_data = {}  # simulation output data

    # function to read FAST output files
    def update(self):
        pass

    # update new parameters to the main loop
    def result(self):
        pass

    # run openMDAO
    def run(self):
        self.logger.info("Running openMDAO optimisation.")
        self.openMDAO.run(self.inputs, self.simulation_data)
        return self
