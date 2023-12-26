from src.Geom.Vector import *


class Line:

    def __init__(self, point_a, point_b):
        self.__point_a = point_a
        self.__point_b = point_b

    def get_point_a(self):
        return self.__point_a

    def get_point_b(self):
        return self.__point_b

    def to_direction_vector(self):
        vector_point = []
        for a, b in zip(self.__point_a, self.__point_b):
            vector_point.append(b - a)
        return Vector(vector_point)
