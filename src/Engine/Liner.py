from src.Shape.Line import Line
from src.Shape.Rectangle import Rectangle


class Liner:
    
    def line_rectangle(self, rectangle):
        return (
            Line(rectangle.get_top_left_point(), rectangle.get_top_right_point()),
            Line(rectangle.get_top_right_point(), rectangle.get_bottom_right_point()),
            Line(rectangle.get_bottom_right_point(), rectangle.get_bottom_left_point()),
            Line(rectangle.get_bottom_left_point(), rectangle.get_top_left_point())
        )
    
    def line_cube(self, cube):
    
        rect_a = Rectangle(cube.get_top_left_point(), cube.get_length(), cube.get_length())
        rect_b = Rectangle(
            (
                cube.get_top_left_point()[0],
                cube.get_top_left_point()[1],
                cube.get_top_left_point()[2] + cube.get_length()
            ),
            cube.get_length(),
            cube.get_length()
        )

        return self.line_rectangle(rect_a) + self.line_rectangle(rect_b) + (
            Line(rect_a.get_top_left_point(), rect_b.get_top_left_point()),
            Line(rect_a.get_top_right_point(), rect_b.get_top_right_point()),
            Line(rect_a.get_bottom_right_point(), rect_b.get_bottom_right_point()),
            Line(rect_a.get_bottom_left_point(), rect_b.get_bottom_left_point())
        )
        