# class for running openFAST
class MDAO:
    def __init__(self, logger):
        self.logger = logger

    # read one simulation output data
    def read(self, key):
        pass

    # sent simulation output
    def sent(self):
        pass

    # receive optimization data
    def receive(self):
        pass

    # run openMDAO
    def run(self):
        self.logger.info("Running openMDAO optimisation.")
