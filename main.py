from turtle import Turtle
from src.Engine.Drawner import Drawner
from src.Engine.Liner import Liner
from src.Shape.Cube import Cube
from src.Transformation.Projection import Projection
from src.Engine.Transformer import Transformer
from src.Transformation.Translation import Translation


def main(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    eye_distance = -300

    turtle = Turtle()
    drawner = Drawner(turtle)
    drawner.drawn_cartesian()

    liner = Liner()
    transformer = Transformer()

    lines = liner.line_cube(Cube((-50, 50, 0), 100))

    lines = transformer.transform_lines(
        lines,
        Translation((-100, -100)).get_transformation_matrix()
    )

    lines = transformer.transform_lines(
        lines,
        Projection(eye_distance).get_transformation_matrix()
    )
    drawner.drawn_lines(lines)

    drawner.reset_cursor()
    turtle.screen.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('caporal')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
