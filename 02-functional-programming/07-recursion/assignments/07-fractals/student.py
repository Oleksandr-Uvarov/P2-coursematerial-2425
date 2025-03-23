import turtle

SPEED = 5
BG_COLOR = "blue"
PEN_COLOR = "lightgreen"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
DRAWING_WIDTH = 700
DRAWING_HEIGHT = 700
PEN_WIDTH = 5
TITLE = "H-Tree Fractal with Python Turtle Graphics"
FRACTAL_DEPTH = 5


def draw_line(tur, pos1, pos2):
    print("Drawing from", pos1, "to", pos2)  # Uncomment for tracing the algorithm.
    tur.penup()
    tur.goto(pos1[0], pos1[1])
    tur.pendown()
    tur.goto(pos2[0], pos2[1])
    
    
def draw_line_in_angle(tur, length, angle):
    tur.setheading(angle)
    tur.forward(length)
    x, y = tur.position()
    tur.backward(length)  # Move back
    return (x, y)
    
# tur = the instance of a turtle object, we need to pass this to the draw_line function to draw lines.
# x = the X-coordinate to start drawing from
# y = the Y-coordinate to start drawing from
# length = The length of the current branch.
# angle = The angle between branches.
# count = the depth of the recursive element at this point.
def recursive_draw(tur, x, y, length, angle, count):
    print(f"Current x, y:  {x}, {y}")
    x_1, y_1 = draw_line_in_angle(tur, length//2, angle)
    draw_line(
        tur,
        [x_1, y_1],
        [x_1 + length // 2, y_1 + length // 2]
    )
    # draw_line(
    #     tur,
    #     [x_1, y_1],
    #     [x_1 + length // 2, y_1 + length // 2]
    # )

    # maybe change back to FRACTAL_DEPTH = 5


    # TODO: implement so a Y-tree is drawn
    if count <= 0:
        return
    else:
        count -= 1
        recursive_draw(tur, x, y, length, angle, count)
        # recursive_draw(tur, x, y, length, 45, count)
        # recursive_draw(tur, x, y, length, 315, count)
    # draw_line(tur, x, y)


if __name__ == "__main__":
    # Screen setup
    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.title(TITLE)
    screen.bgcolor(BG_COLOR)

    # Turtle artist (pen) setup
    tur = turtle.Turtle()
    tur.hideturtle()
    tur.pensize(PEN_WIDTH)
    tur.color(PEN_COLOR)
    tur.speed(SPEED)

    # Initial call to recursive draw function
    recursive_draw(tur, 0, -SCREEN_HEIGHT // 3, DRAWING_HEIGHT // 4, 90, FRACTAL_DEPTH)

    # Every Python Turtle program needs this (or an equivalent) to work correctly.
    turtle.done()






# abcd
# take a away, store it; we have bcd left
# take b away, store it; we have b left
# 