from src.Shape.Line import Line


class Transformer:

    def transform_lines(self, lines, transformation_matrix):
        result = []
        for line in lines:
            result.append(Line(
                self.transform_vector(line.get_point_a(), transformation_matrix),
                self.transform_vector(line.get_point_b(), transformation_matrix)
            ))
        return result

    def transform_matrix(self, matrix, transformation_matrix):
        result = []
        for i, vectors in enumerate(matrix):
            result.insert(i, self.translate_vectors(vectors, transformation_matrix))
        return result

    def transform_vectors(self, vectors, transformation_matrix):
        result = []
        for i, vector in enumerate(vectors):
            result.insert(i, self.transform_vector(vector, transformation_matrix))
        return result

    def transform_vector(self, vector, transformation_matrix):
        result = []
        for i, row in enumerate(transformation_matrix):
            result.insert(i, 0)
            for j, cell in enumerate(row):
                value = 1
                if j < len(vector):
                    value = vector[j]
                result[i] += cell * value
        return self.transform_homogeneous_to_cartesian_coordinates(result)

    def transform_homogeneous_to_cartesian_coordinates(self, homogeneous_coordinates):
        result = []
        homogeneous_value = homogeneous_coordinates[-1]
        for i in range(0, len(homogeneous_coordinates)):
            result.append(homogeneous_coordinates[i] * homogeneous_value)
        return result
