import turtle

# Function to draw a character
def draw_character(color, shape, x, y):
    character = turtle.Turtle()
    character.shape(shape)
    character.color(color)
    character.penup()
    character.goto(x, y)
    return character

# Draw Tom
def draw_tom():
    tom = draw_character("blue", "circle", -100, 0)
    return tom

# Draw Jerry
def draw_jerry():
    jerry = draw_character("brown", "circle", 100, 0)
    return jerry

# Draw the scene
def draw_scene():
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Tom and Jerry")

    tom = draw_tom()
    jerry = draw_jerry()

    # Add more details to the characters or the background if desired

    turtle.done()

# Main function
if __name__ == "__main__":
    draw_scene()
