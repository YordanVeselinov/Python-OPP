from abc import ABC, abstractmethod


class Robot(ABC):

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("Robot can not be created without a name")
        self.__name = value

    @staticmethod
    @abstractmethod
    def sensors_amount():
        pass


class MedicalRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 6


class ChefRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 4


class WarRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 12


class AIRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 12


class NewAgeRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 32


def number_of_robot_sensors(robot):
    print(robot.sensors_amount())


