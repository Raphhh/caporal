from src.Shape.Line import Line
from src.Shape.Rectangle import Rectangle


class Cube:

    def __init__(self, top_left_point, length):
        self.__top_left_point = top_left_point
        self.__length = length

    def get_top_left_point(self):
        return self.__top_left_point

    def get_length(self):
        return self.__length