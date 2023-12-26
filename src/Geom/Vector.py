from src.Geom.Angle import *
import math


class Vector:

    def __init__(self, point):
        self.__point = point

    def get_point(self):
        return self.__point

    def get_magnitude(self):
        # return math.sqrt(sum([value**2 for value in self.__point]))
        # only 2D:
        return math.sqrt((self.__point[0]**2) + (self.__point[1]**2))

    def get_direction(self):
        if self.__point[0] < 0:
            return -1
        return 1

    def get_directed_magnitude(self):
        return self.get_magnitude() * self.get_direction()

    def get_angle(self):
        if self.__point[0] == 0:
            if self.__point[1] >= 0:
                return Angle(90)
            return Angle(-90)

        div = self.__point[1] / self.__point[0]
        return Angle(math.degrees(math.atan(div)))



