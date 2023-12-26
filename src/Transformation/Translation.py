class Translation:

    def __init__(self, vector, homogeneous_value=1):
        self.__vector = vector
        self.__homogeneous_value = homogeneous_value

    def get_transformation_matrix(self):

        # matrix = (
        #    (1, 0, translation[0]),
        #    (0, 1, translation[1]),
        #    (0, 0, homogeneous_value)
        # )

        return (
            (1, 0, 0, self.__vector[0]),
            (0, 1, 0, self.__vector[1]),
            (0, 0, 1, 0),
            (0, 0, 0, self.__homogeneous_value)
         )

        matrix = []
        for i in range(0, len(self.__vector) + 1):
            matrix.insert(i, [])
            for j in range(0, len(self.__vector) + 1):
                if j == len(self.__vector):
                    if i < len(self.__vector):
                        matrix[i].insert(j, self.__vector[i])
                    else:
                        matrix[i].insert(j, self.__homogeneous_value)
                elif i == j:
                    matrix[i].insert(j, 1)
                else:
                    matrix[i].insert(j, 0)
        return matrix
