# API for changing the input files
class File_api:
    def __init__(self, logger, path):
        self.logger = logger
        self.path = path
        self.file = open(self.path)

    # function to change .dat or .fst files in openFAST
    def change_fast(self, key, value):
        pass

    # function to change .m file for generating the .gdf file
    def change_m(self, line, value):
        pass

    # function to change WAMIT input files
    def change_wamit(self, line, value):
        pass

    # function to read FAST output files
    def read_fast(self):
        pass

    # return file path
    def read_path(self):
        return self.file.name

    # open file
    def open(self, path):
        self.path = path
        self.file = open(self.path)
