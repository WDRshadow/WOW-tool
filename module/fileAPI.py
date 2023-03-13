import os
import shutil

from module import logger


class FileAPI:
    def __init__(self, path: str, name: str):
        """
        A class of file modified API. This class is used to change, read, move, rename a file in the project.
        :param path: The relative path of the modified file.
        :param name: The file name.
        """
        self.logger = logger.logger
        self.path = path
        self.name = name

    def __del__(self):
        pass

    def changer(self):
        """
        Get a Changer object for modifying several values of the same file in succession.
        :return: a Changer object.
        """
        return Changer(self)

    def reader(self):
        """
        Get a Reader object for reading several values of the same file in succession.
        :return: a Reader object.
        """
        return Reader(self)

    def rename(self, name: str):
        """
        A function to rename this data storage file.
        :param name: New name.
        :return: The object.
        """
        try:
            os.rename(os.path.join(self.path, self.name), os.path.join(self.path, name))
            self.name = name
            return self
        except Exception as err:
            self.logger.error("Cannot rename file " + self.name)
            self.logger.error(err)
            exit()

    def move(self, newPath: str):
        """
        A function to move this data storage file to a new path.
        :param newPath: The new location for the file.
        :return: The object.
        """
        try:
            shutil.move(os.path.join(self.path, self.name), newPath)
            self.path = newPath
            return self
        except Exception as err:
            self.logger.error("Cannot move file " + self.name + " to " + newPath)
            self.logger.error(err)
            exit()

    def copy(self, newPath: str):
        """
        A function to copy this data storage file to a new path.
        :param newPath: The new path for the file.
        :return: A new object for the new file.
        """
        try:
            shutil.copy(os.path.join(self.path, self.name), newPath)
            return FileAPI(newPath, self.name)
        except Exception as err:
            self.logger.error("Cannot move file " + self.name + " to " + newPath)
            self.logger.error(err)
            exit()

    def remove(self):
        """
        A function to remove the file and delete the object.
        :return: void.
        """
        try:
            os.remove(os.path.join(self.path, self.name))
            self.__del__()
        except Exception as err:
            self.logger.error("Cannot remove file " + self.name)
            self.logger.error(err)
            exit()

    def isExist(self):
        """
        A function to check if the file exist.
        :return: True if it is exist or, False if it is not.
        """
        return os.path.exists(os.path.join(self.path, self.name))


class Changer:
    def __init__(self, file: FileAPI):
        """
        A changer class for modifying several values of the same file in succession.
        :param file: A object of FileAPI class.
        """
        self.file = file
        try:
            self.lines = open(os.path.join(self.file.path, self.file.name)).readlines()
        except Exception as err:
            self.file.logger.error("Cannot open file " + self.file.name)
            self.file.logger.error(err)
            exit()

    def change(self, line: int, value: str, val_l: int):
        """
        A function to change a value in this data storage file.
        :param line: The line where the changing value is.
        :param value: Modified values (new).
        :param val_l: The location of the changing value in the line (divided by a space).
        :return: Changer object.
        """
        val = self.lines[line - 1].split()
        self.lines[line - 1] = self.lines[line - 1].replace(val[val_l - 1], value)
        return self

    def do(self):
        """
        Confirm and implement the changing.
        :return: The class FileAPI object.
        """
        try:
            with open(os.path.join(self.file.path, self.file.name), "w") as file:
                file.writelines(self.lines)
            return self
        except Exception as err:
            self.file.logger.error("Cannot open file " + self.file.name)
            self.file.logger.error(err)
            exit()
        return self.file


class Reader:
    def __init__(self, file: FileAPI):
        """
        A changer class for reading several values of the same file in succession.
        :param file: A object of FileAPI class.
        """
        self.value = []
        try:
            self.lines = open(os.path.join(file.path, file.name)).readlines()
        except Exception as err:
            file.logger.error("Cannot open file " + file.name)
            file.logger.error(err)
            exit()

    def read(self, line: int, val_l: int):
        """
        A function to read a value in this data storage file.
        :param line: The line where the value is.
        :param val_l: The location of the value in the line (divided by a space).
        :return: Reader object.
        """
        self.value.append(self.lines[line - 1].split()[val_l - 1])
        return self

    def result(self):
        """
        Get the result of all the reading values.
        :return: The values.
        """
        return self.value
