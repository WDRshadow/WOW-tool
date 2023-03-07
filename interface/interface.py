from abc import ABCMeta, abstractmethod


# class for running openMDAO and transfer the data between simulation and optimization
class OpenMDAO:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        """
        Saving the parameters we need for simulation.
        """
        self.column_radius = float
        self.column_height = float
        self.column_distance = float
        self.tower_height = float
        self.draft = float
        self.hp_radius = float  # Radius of Heave plate
        self.data = None  # Other variables you need or we need

    @abstractmethod
    def run(self, data):
        """
        This method should run openMDAO with some simulation result data
        :param data: tell me what input data you need?
        :return: You should save the optimization data in some where (Variables in the class will be better.)
        """
        pass

    # return the result of optimization
    @abstractmethod
    def sent_result(self):
        """
        This method should return the optimization result to us.
        :return: The result should at least includes the column radius, height, tower height,
        distance between columns, draft.
        """
        return self.column_radius, self.column_height, self.column_distance, self.tower_height, self.hp_radius
