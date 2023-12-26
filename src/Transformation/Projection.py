
class Projection:

    def __init__(self, distance, homogeneous_value=1):
        if distance == 0:
            raise Exception('distance of projection must not be 0')
        self.__distance = distance
        self.__homogeneous_value = homogeneous_value

    def get_transformation_matrix(self):

        return (
            (1, 0, 0, 0),
            (0, 1, 0, 0),
            (0, 0, 0, 0),
            (0, 0, 1/self.__distance, self.__homogeneous_value)
        )
