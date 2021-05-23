"""
Created by Zeynep ÖZDEMİR, ÖZGE MERCANOĞLU SİNCAN
"""
from graphics import *
import random

# Do not change these following 4 variables
margin = 10  # height of the paddle from the ground
moveIncrement = 15  # paddle movement
ballRadius = 15
BOUNCE_WAIT = 1200
lives = 2

BALL_COUNT = 3  # If we change this, the number of ball changes!


class Timer:
    def __init__(self):
        self.value = 0


class Paddle:

    def __init__(self, color, width, height, coordx, win):
        self.color = color
        self.width = width
        self.height = height
        self.x = coordx
        self.shape = Rectangle(Point(self.x - int(self.width / 2), win.getHeight() - margin - self.height),
                               Point(self.x + int(self.width / 2), win.getHeight() - margin))
        self.shape.setFill(self.color)
        self.window = win
        self.shape.draw(self.window)

    def move_left(self):   # move paddle to the left by the amount of global variable moveIncrement
        if not self.shape.getCenter().x <= 50:
            self.x -= moveIncrement
            self.shape.move(-moveIncrement, 0)

    def move_right(self):  # move paddle to the right by the amount of global variable moveIncrement
        if not self.shape.getCenter().x >= 250:
            self.x += moveIncrement
            self.shape.move(moveIncrement, 0)


class Bubbles:
    # Define it by yourself to implement bubbles in the assignment
    def __init__(self, line, radius, x, win, color):
        self.shape = Circle(Point(x, (30+60*line)), radius)
        self.shape.draw(win)
        self.shape.setFill(color)
        self.center = Point(x, (30+60*line))
        self.radius = radius

    def remove(self):
        global bubbleList
        try:
            bubbleList.remove(self)
            self.shape.undraw()
        except:
            pass




class Ball:

    def __init__(self, coordx, coordy, color, radius, x_direction, speed, win):
        self.shape = Circle(Point(coordx, coordy), radius)
        self.x = coordx
        self.y = coordy
        self.xMovement = 0  # Current x movement
        self.yMovement = 0  # Current y movement
        self.color = color
        self.window = win
        self.shape.setFill(self.color)
        self.shape.draw(self.window)
        self.radius = radius
        self.timer = 0
        self.x_direction = x_direction   # Initial x direction. This variable will be 0 or 1. 1:right 0:left
        self.speed = speed

    def is_moving(self):
        if self.xMovement != 0:
            return True
        else:
            return False

    def bounce(self, gameTimer, minX, maxX, maxY, bubbList):
        # Calculating x-axis ball movement and bouncing
        # minX: min x coord. of paddle
        # maxX: max x coord. of paddle
        # maxY: max y coord. at which the ball can be move. If it goes further, it falls to the ground.

        global BOUNCE_WAIT, win
        gameOver = False
        if gameTimer >= self.timer + BOUNCE_WAIT:
            self.timer = gameTimer
            for i in bubbList:
                if ((i.center.x-self.shape.getCenter().x)**2) + ((i.center.y-self.shape.getCenter().y)**2) < (i.radius+self.radius)**2:
                    i.remove()
            if self.xMovement == 1:
                self.x += self.speed
            elif self.xMovement == -1:
                self.x -= self.speed
            if self.shape.getCenter().x >= 300-self.radius:
                self.xMovement = -self.xMovement
            elif self.shape.getCenter().x <= 0+self.radius:
                self.xMovement = -self.xMovement
            if self.shape.getCenter().y <= 0+self.radius:
                self.yMovement = -self.yMovement
            if maxY+1-self.radius+self.speed >= self.shape.getCenter().y >= maxY+1-self.radius and minX < self.shape.getCenter().x < maxX:
                self.yMovement = -self.yMovement
            if self.shape.getCenter().y >= maxY+margin+self.radius:
                gameOver = True
            self.shape.move(self.xMovement * self.speed, self.yMovement * self.speed)
            return gameOver

def remove(list):
    for i in list:
        try:
            i.shape.undraw()
        except:
            pass


win = GraphWin("19290315 Pong Game", 300, 600) # Replace your student id
win.setBackground("Black")
bubbleList = []

def main():
    global lives, win, bubbleList
    myPaddle = Paddle("White", 100, 15, 150, win)

    ColorsList = ["Cyan","Red","Green","Yellow"]
    BallList = list()
    for i in range(BALL_COUNT):
        rand_speed = random.randint(5, 20) # random speed for ball
        rand_direction = random.randint(0, 1) # This variable will be 0 or 1 randomly.
        ball = Ball(myPaddle.x - int(myPaddle.width/2) + i*30, win.getHeight() - margin - myPaddle.height - ballRadius, ColorsList[i%4] , ballRadius,rand_direction,rand_speed, win)
        BallList.append(ball)

    bubbleColorList = ["Purple", "Blue", "WhiteSmoke"]
    bubbleList = []
    for i in range(3):
        for l in range(5):
            bubb = Bubbles(i, 30, (30+l*60), win, bubbleColorList[i%3])
            bubbleList.append(bubb)

    livesCounter = Text(Point(win.getWidth() - int(win.getWidth() / 5), 250), f'Lives -- {lives}')
    livesCounter.setTextColor("Cyan")
    livesCounter.setSize(15)
    try:
        livesCounter.undraw()
    except:
        pass
    livesCounter.draw(win)
    gameTimer = Timer()
    livesCounter.setFace("courier")
    gameOverT = Text(Point(win.getWidth() - int(win.getWidth() / 2), 300), "GAME OVER")
    youLost = Text(Point(win.getWidth() - int(win.getWidth() / 2), 335), "YOU LOST!")
    youWin = Text(Point(win.getWidth() - int(win.getWidth() / 2), 335), "YOU WIN!")
    anyKey = Text(Point(150, 370), "Press Any Key to Quit")
    List0 = [gameOverT, youLost, youWin, anyKey]
    for i in List0:
        i.setFace("courier")
        i.setSize(15)
        i.setStyle("bold")
        i.setTextColor("red")

    gameOver = False

    try:
        while lives > 0:
            while not gameOver:
                keyPress = win.checkKey()
                if keyPress == 'a':
                    myPaddle.move_left()

                if keyPress == 'd':
                    myPaddle.move_right()

                if keyPress == 'l':  # balls will move faster
                    for item in BallList:
                        item.speed += 1

                if keyPress == 'k':  # Balls will move slower. Note that in our case min speed is 2.
                    for item in BallList:
                        if item.speed > 2:
                            item.speed -= 1

                if keyPress == 's':  # Initial movement of balls
                    for item in BallList:
                        if not item.is_moving():
                            if item.x_direction == 1:   # it means ball moves to right in x direction
                                item.xMovement = 1
                            else:                   # it means ball moves to left in x direction
                                item.xMovement = -1
                            item.yMovement = -1  # at initial ball moves up in y direction
                if bubbleList == []:
                    lives = -1
                    remove(BallList)
                    remove(bubbleList)
                    myPaddle.shape.undraw()
                    gameOverT.draw(win)
                    youWin.draw(win)
                    anyKey.draw(win)
                    win.getKey()
                    win.close()
                    break
                gameTimer.value += 1
                for item in BallList:
                    gameOver = item.bounce(gameTimer.value, (myPaddle.x-int(myPaddle.width/2)), (myPaddle.x+int(myPaddle.width/2)), win.getHeight() - margin - myPaddle.height, bubbleList)
                    if gameOver:
                        lives -= 1
                        remove(BallList)
                        remove(bubbleList)
                        livesCounter.undraw()
                        myPaddle.shape.undraw()
                        main()
                        break
    except:
        win.close()
    if lives == 0:
        try:
            remove(BallList)
            remove(bubbleList)
            myPaddle.shape.undraw()
            gameOverT.draw(win)
            youLost.draw(win)
            anyKey.draw(win)
            win.getKey()
            win.close()
        except:
            win.close()


a = 0
if a == 0:
    a += 1
    main()
win.close()
