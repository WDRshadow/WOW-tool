import fnmatch
import os
import subprocess

import config
from module import logger
from module.fileAPI import FileAPI


# class for running openFAST
class FAST:
    def __init__(self):
        self.logger = logger.logger
        self.path = config.openFAST_path

    # update the input files
    def update(self):
        if not os.path.exists(os.path.join(config.openFAST_path, "HydroData")):
            os.makedirs(os.path.join(config.openFAST_path, "HydroData"))
        FileAPI(config.temp_path, "wow.1").copy(os.path.join(self.path, "HydroData"))
        FileAPI(config.temp_path, "wow.3").copy(os.path.join(self.path, "HydroData"))
        FileAPI(config.temp_path, "wow.hst").copy(os.path.join(self.path, "HydroData"))
        '''input files update'''
        return self

    # run openFAST simulation
    def run(self):
        self.logger.info("Running openFAST simulation.")
        for f_name in os.listdir(self.path):
            if fnmatch.fnmatch(f_name, '*.sum') or fnmatch.fnmatch(f_name, '*.out') or \
                    fnmatch.fnmatch(f_name, '*.outb') or fnmatch.fnmatch(f_name, '*.ech') or \
                    fnmatch.fnmatch(f_name, '*.log'):
                FileAPI(self.path, f_name).move(config.temp_path)
        try:
            subprocess.check_call([config.openFAST_command, "main.fst"], cwd=self.path)

        except Exception as err:
            self.logger.error("Run openFAST failed.")
            self.logger.error(err)
            exit()
