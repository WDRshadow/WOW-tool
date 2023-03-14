import config
import subprocess
from module import logger
from module.fileAPI import FileAPI


# class for running WAMIT
class WAMIT:
    def __init__(self):
        self.logger = logger.logger
        self.path = config.wamit_path

    # update input files
    def update(self):
        FileAPI(config.temp_path, "wow.gdf").copy(self.path)
        FileAPI(config.temp_path, "wow.cfg").copy(self.path)
        return self

    # check and make sure there are no output files in the path
    def check(self):
        output_files = ["wow.1", "wow.3", "wow.12d", "wow.hst", "wow.ss", "wow.ssexctn"]
        for i in output_files:
            file = FileAPI(self.path, i)
            if file.isExist():
                file.remove()
        return self

    # calculate the hydrostatic data
    def run(self):
        self.logger.info("Running WAMIT to get the hydrostatic data.")
        try:
            subprocess.check_call(config.wamit_command, cwd=self.path)
            FileAPI(self.path, "wow.1").move(config.temp_path)
            FileAPI(self.path, "wow.3").move(config.temp_path)
            FileAPI(self.path, "wow.hst").move(config.temp_path)
        except Exception as err:
            self.logger.error("Run WAMIT failed.")
            self.logger.error(err)
            exit()
