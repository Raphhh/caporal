class Drawner:

    def __init__(self, graphics_engine):
        self.__graphics_engine = graphics_engine

    def drawn_cartesian(self, scale=100, color='lightgrey'):
        current_color = self.__graphics_engine.pencolor()
        self.__graphics_engine.pencolor(color)

        r_size = 5

        for i in range(0, 4):

            self.__graphics_engine.penup()
            self.__graphics_engine.setx(0)
            self.__graphics_engine.sety(0)
            self.__graphics_engine.pendown()

            self.__graphics_engine.left(90)

            for j in range(0, 3):
                self.__graphics_engine.left(90)
                self.__graphics_engine.forward(r_size)
                self.__graphics_engine.backward(r_size*2)
                self.__graphics_engine.forward(r_size)
                self.__graphics_engine.right(90)
                self.__graphics_engine.forward(scale)

        self.__graphics_engine.penup()
        self.__graphics_engine.setx(0)
        self.__graphics_engine.sety(0)
        self.__graphics_engine.pendown()

        self.__graphics_engine.pencolor(current_color)

    def drawn_lines(self, lines):
        for line in lines:
            self.drawn_line(line)

    def drawn_line(self, line):
        print('-- drawn_line for line (({:0.2f}, {:0.2f}), ({:0.2f}, {:0.2f})) --'.format(
            line.get_point_a()[0],
            line.get_point_a()[1],
            line.get_point_b()[0],
            line.get_point_b()[1]
        ))

        self.set_cursor(line.get_point_a())
        print('actual_start_position({:0.2f}, {:0.2f})'.format(self.__graphics_engine.position()[0], self.__graphics_engine.position()[1]))

        self.__graphics_engine.pendown()

        vector = line.to_direction_vector()
        print('vector_point_position({:0.2f}, {:0.2f})'.format(vector.get_point()[0], vector.get_point()[1]))

        print('left({:0.2f}°)'.format(vector.get_angle().get_degree()))
        self.__graphics_engine.left(vector.get_angle().get_degree())

        print('forward({:0.2f})'.format(vector.get_directed_magnitude()))
        self.__graphics_engine.forward(vector.get_directed_magnitude())

        print('right({:0.2f}°)'.format(vector.get_angle().get_degree()))
        self.__graphics_engine.right(vector.get_angle().get_degree())

        print('expected_end_position({:0.2f}, {:0.2f})'.format(line.get_point_b()[0], line.get_point_b()[1]))
        print('actual_end_position({:0.2f}, {:0.2f})'.format(self.__graphics_engine.position()[0], self.__graphics_engine.position()[1]))

    def set_cursor(self, point):
        self.__graphics_engine.penup()
        self.__graphics_engine.setx(point[0])
        self.__graphics_engine.sety(point[1])

    def reset_cursor(self):
        self.set_cursor((0, 0))
