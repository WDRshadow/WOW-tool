import os
import re
from module import logger


# check folder exist
def init_check():
    folder_list = ["MATLAB", "WAMIT", "openFAST", "temp", "logs"]
    for i in folder_list:
        folder = os.path.exists(i)
        if not folder:
            os.makedirs(i)


# API for changing the input files
class FileAPI:
    def __init__(self, path):
        self.logger = logger.logger
        self.path = path
        self.end = re.search("\.\w+$", path).group()
        self.key_l = int
        self.val_l = int
        if self.end == ".m":
            self.key_l = 1
            self.val_l = 3
        elif self.end == ".dat" or ".fst":
            self.key_l = 2
            self.val_l = 1
        # for WAMIT and else

    # get location
    def loc(self, key_l, val_l):
        if key_l is None:
            if self.key_l is None:
                logger.logger.error("Miss key location.")
                exit()
            key_l = self.key_l
        if val_l is None and self.val_l is not None:
            if self.val_l is None:
                logger.logger.error("Miss value location.")
                exit()
            val_l = self.val_l
        return key_l, val_l

    # change a specific value with key and line information
    def change(self, line, key, value, key_l=None, val_l=None):
        key_l, val_l = self.loc(key_l, val_l)
        try:
            file = open(self.path)
            lines = file.readlines()
            file.close()
            val = lines[line - 1].split()
            if val[key_l - 1] == key:
                lines[line - 1] = lines[line - 1].replace(val[val_l - 1], value)
            else:
                logger.logger.error("Cannot find key " + key)
                exit()
            file = open(self.path, "w")
            file.writelines(lines)
            file.close()
        except Exception as err:
            logger.logger.error("Cannot open file " + self.path)
            logger.logger.error(err)
            exit()

    # get a specific value with key and line information
    def read(self, line, key, key_l=None, val_l=None):
        key_l, val_l = self.loc(key_l, val_l)
        try:
            file = open(self.path)
            lines = file.readlines()
            file.close()
            val = lines[line - 1].split()
            if val[key_l - 1] == key:
                return val[val_l - 1]
            else:
                logger.logger.error("Cannot find key " + key)
                exit()
        except Exception as err:
            logger.logger.error("Cannot open file " + self.path)
            logger.logger.error(err)
            exit()
