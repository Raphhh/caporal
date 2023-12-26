
class Rectangle:

    def __init__(self, top_left_point, height, width):
        self.__top_left_point = top_left_point
        self.__height = height
        self.__width = width

    def get_top_left_point(self):
        return self.__top_left_point

    def get_top_right_point(self):
        return self.__top_left_point[0] + self.__width, \
            self.__top_left_point[1], \
            self.__top_left_point[2]

    def get_bottom_right_point(self):
        return self.__top_left_point[0] + self.__width, \
            self.__top_left_point[1] - self.__height, \
            self.__top_left_point[2]

    def get_bottom_left_point(self):
        return self.__top_left_point[0], \
            self.__top_left_point[1] - self.__height, \
            self.__top_left_point[2]

    def get_height(self):
        return self.__height

    def get_width(self):
        return self.__width
