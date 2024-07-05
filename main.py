import turtle
from random import randint, choice
# Initialize the turtle screen
screen = turtle.Screen()
screen.setup(width=500, height=600)  # Set the screen dimensions
screen.title("Turtle Paddle Party")  # Set the title of the window
screen.bgcolor("white")  # Set the background color

blocks={}
dict ={}
bot = 0
num_blocks = 0
turtle_colors = [
    "black",
    "red",
    "green",
    "blue",
    "cyan",
    "magenta",
    "yellow",
    "orange",
    "brown",
    "pink",
    "purple",
    "gray",
    "lightgray",
    "darkgray",
]
def twelve():
    list = []
    list_one = []
    a = -240
    while sum(list) != 17:
        list.append(randint(1, 5))
        if sum(list) > 17:
            list = []
    for i in range(len(list)):
        if list[i-1]:
            a += (list[i -1] + list[i]) * 12
        list_one.append(a)
    return [list, list_one]

class Block(turtle.Turtle):
    def __init__(self, colo, length, x, y):
        super().__init__()
        self.shape('square')
        self.penup()
        self.speed(10)
        self.color(colo)
        self.shapesize(stretch_wid=0.5, stretch_len=length, outline=1)
        self.goto(x,y)


class Paddle(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.color('black')
        self.goto(x=0, y=-200)
        self.shapesize(stretch_wid=0.8, stretch_len=6)
        self.setheading(0)

    def move_right(self):
        new_x = self.xcor() + 10  # Move right by 10 units
        self.setx(new_x)

    def move_left(self):
        new_x = self.xcor() - 10  # Move left by 10 units
        self.setx(new_x)

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.color('blue')
        self.goto(x=0, y=-150)
        self.setheading(270)

    def move(self, paddle):
        global bot
        self.forward(4)
        pad_x = int(paddle.pos()[0])
        x, y = self.pos()
        ratio = (int(round(x, 1)) - pad_x)/ 70

        if bot > 0:
            bot -= 1
        if bot == 0:
            if y <= -180 and int(round(x, 1)) in range(pad_x - 70, pad_x + 70):
                self.bottom_bounce(ratio)
                self.forward(8)
                bot += 6


        if y > 290:
            self.top_bounce()
            self.forward(8)

        if x >=  230 or x <= -240:
            self.side_bounce()
            self.forward(20)
        if_break(num_blocks)

        if y < -300:
            turtle.bye()

        if len(blocks) == 0:
            screen.clear()
            spiral = turtle.Turtle()
            spiral.speed(0)
            spiral.color("cyan")
            # Draw the spiral
            for i in range(100):
                spiral.forward(i * 10)
                spiral.right(144)

            # Hide the turtle
            spiral.hideturtle()

            # Keep the window open
            screen.mainloop()
        print(len(blocks))
        screen.ontimer(lambda: self.move(paddle=paddle), 10)


    def side_bounce(self):
        ang = self.heading()
        self.setheading(180-ang)


    def top_bounce(self):
        ang = self.heading()
        self.setheading(360 - ang)

    def bottom_bounce(self, ratio):
        self.setheading(self.heading() - 180)
        self.setheading(self.heading() + (ratio * 30))

def if_break(num):
    if y > 0:
        for i in range(0, num):
            if i in blocks:
                pos_x, pos_y = ball.pos()
                pos_y = int(pos_y)
                pos_x = int(pos_x)
                if pos_x in range(dict[i]['x'] - (20 * dict[i]['length']), dict[i]['x'] + (dict[i]['length'] * 20)):
                    if pos_y in range(dict[i]['y'] -10, dict[i]['y'] + 10):
                        blocks[i].hideturtle()
                        del blocks[i]
                        if pos_y < dict[i]['y']:
                            ball.bottom_bounce(1)
                        else:
                            ball.top_bounce()

brock = 0

for i in range(0, 8):
    twelov = twelve()
    y = 250 - (i * 20)
    num_blocks += len(twelov[0])
    for i in range(len(twelov[0])):
        x = twelov[1][i]
        length = twelov[0][i]
        block = Block(colo=choice(turtle_colors), length=length, x=x, y=y)
        blocks[brock] = block
        dict[brock] = {'x': x, 'y': y, 'length': length}
        brock += 1

paddle = Paddle()
ball = Ball()
ball.move(paddle=paddle)
screen.listen()
screen.onkeypress(paddle.move_left, "Left")
screen.onkeypress(paddle.move_right, "Right")
turtle.done()
