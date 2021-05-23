import random
from graphics import *

winst = False
STATUS = "XTURN"
a, aX, aY = None, None, None
Filled = []
winCheck = []
win = GraphWin("19290315", 300, 350)
xLine1 = Line(Point(0, 0), Point(294, 0))
xLine2 = Line(Point(0, 100), Point(294, 100))
xLine3 = Line(Point(0, 200), Point(294, 200))
xLine4 = Line(Point(0, 300), Point(294, 300))
yLine1 = Line(Point(0, 0), Point(0, 300))
yLine2 = Line(Point(98, 0), Point(98, 300))
yLine3 = Line(Point(196, 0), Point(196, 300))
yLine4 = Line(Point(294, 0), Point(294, 300))
myList = [xLine1, xLine2, xLine3, xLine4, yLine1, yLine2, yLine3, yLine4]
for i in myList:
    i.draw(win)

X1 = Text(Point(49, 50), "X")
X2 = Text(Point(49, 150), "X")
X3 = Text(Point(49, 250), "X")
X4 = Text(Point(147, 50), "X")
X5 = Text(Point(147, 150), "X")
X6 = Text(Point(147, 250), "X")
X7 = Text(Point(245, 50), "X")
X8 = Text(Point(245, 150), "X")
X9 = Text(Point(245, 250), "X")
O1 = Text(Point(49, 50), "O")
O2 = Text(Point(49, 150), "O")
O3 = Text(Point(49, 250), "O")
O4 = Text(Point(147, 50), "O")
O5 = Text(Point(147, 150), "O")
O6 = Text(Point(147, 250), "O")
O7 = Text(Point(245, 50), "O")
O8 = Text(Point(245, 150), "O")
O9 = Text(Point(245, 250), "O")
warn = Text(Point(150, 325), "You cannot click the filled squares!")
owin = Text(Point(150, 325), "O Wins")
xwin = Text(Point(150, 325), "X Wins")
draw = Text(Point(150, 325), "Draw!")


def tryBlock():
    try:
        warn.draw(win)
    except GraphicsError:
        pass


def mouseEntry():
    global STATUS, a, aX, aY, Filled
    if STATUS == "XWIN":
        try:
            xwin.draw(win)
        except:
            pass
        c = win.getKey()
        if c == "q" or c == "Q":
            win.close()
        else:
            mouseEntry()
    elif STATUS == "OWIN":
        try:
            owin.draw(win)
        except:
            pass
        c = win.getKey()
        if c == "q" or c == "Q":
            win.close()
        else:
            mouseEntry()
    elif STATUS == "DRAW":
        try:
            draw.draw(win)
        except:
            pass
        c = win.getKey()
        if c == "q" or c == "Q":
            win.close()
        else:
            mouseEntry()
    elif STATUS == "XTURN":
        a = win.getMouse()
        aX = a.getX()
        aY = a.getY()
        if 0 < aX < 98 and 0 < aY < 100:
            if 1 not in Filled:
                X1.draw(win)
                Filled.append(1)
                winCheck.append("x1")
                warn.undraw()
                STATUS = "OTURN"
            else:
                tryBlock()
        if 0 < aX < 98 and 100 < aY < 200:
            if 2 not in Filled:
                X2.draw(win)
                Filled.append(2)
                winCheck.append("x2")
                warn.undraw()
                STATUS = "OTURN"
            else:
                tryBlock()
        if 0 < aX < 98 and 200 < aY < 300:
            if 3 not in Filled:
                X3.draw(win)
                Filled.append(3)
                winCheck.append("x3")
                warn.undraw()
                STATUS = "OTURN"
            else:
                tryBlock()
        if 98 < aX < 196 and 0 < aY < 100:
            if 4 not in Filled:
                X4.draw(win)
                Filled.append(4)
                winCheck.append("x4")
                warn.undraw()
                STATUS = "OTURN"
            else:
                tryBlock()
        if 98 < aX < 196 and 100 < aY < 200:
            if 5 not in Filled:
                X5.draw(win)
                Filled.append(5)
                winCheck.append("x5")
                warn.undraw()
                STATUS = "OTURN"
            else:
                tryBlock()
        if 98 < aX < 196 and 200 < aY < 300:
            if 6 not in Filled:
                X6.draw(win)
                Filled.append(6)
                winCheck.append("x6")
                warn.undraw()
                STATUS = "OTURN"
            else:
                tryBlock()
        if 196 < aX < 294 and 0 < aY < 100:
            if 7 not in Filled:
                X7.draw(win)
                Filled.append(7)
                winCheck.append("x7")
                warn.undraw()
                STATUS = "OTURN"
            else:
                tryBlock()
        if 196 < aX < 294 and 100 < aY < 200:
            if 8 not in Filled:
                X8.draw(win)
                Filled.append(8)
                winCheck.append("x8")
                warn.undraw()
                STATUS = "OTURN"
            else:
                tryBlock()
        if 196 < aX < 294 and 200 < aY < 300:
            if 9 not in Filled:
                X9.draw(win)
                Filled.append(9)
                winCheck.append("x9")
                warn.undraw()
                STATUS = "OTURN"
            else:
                tryBlock()
    elif STATUS == "OTURN":
        rand = random.choice(list({1, 2, 3, 4, 5, 6, 7, 8, 9} - set(Filled)))
        if rand == 1:
            if 1 not in Filled:
                O1.draw(win)
                Filled.append(1)
                winCheck.append("o1")
                warn.undraw()
                STATUS = "XTURN"
        if rand == 2:
            if 2 not in Filled:
                O2.draw(win)
                Filled.append(2)
                winCheck.append("o2")
                warn.undraw()
                STATUS = "XTURN"
        if rand == 3:
            if 3 not in Filled:
                O3.draw(win)
                Filled.append(3)
                winCheck.append("o3")
                warn.undraw()
                STATUS = "XTURN"
        if rand == 4:
            if 4 not in Filled:
                O4.draw(win)
                Filled.append(4)
                winCheck.append("o4")
                warn.undraw()
                STATUS = "XTURN"
        if rand == 5:
            if 5 not in Filled:
                O5.draw(win)
                Filled.append(5)
                winCheck.append("o5")
                warn.undraw()
                STATUS = "XTURN"
        if rand == 6:
            if 6 not in Filled:
                O6.draw(win)
                Filled.append(6)
                winCheck.append("o6")
                warn.undraw()
                STATUS = "XTURN"
        if rand == 7:
            if 7 not in Filled:
                O7.draw(win)
                Filled.append(7)
                winCheck.append("o7")
                warn.undraw()
                STATUS = "XTURN"
        if rand == 8:
            if 8 not in Filled:
                O8.draw(win)
                Filled.append(8)
                winCheck.append("o8")
                warn.undraw()
                STATUS = "XTURN"
        if rand == 9:
            if 9 not in Filled:
                O9.draw(win)
                Filled.append(9)
                winCheck.append("o9")
                warn.undraw()
                STATUS = "XTURN"


while True:
    if "x1" in winCheck and "x2" in winCheck and "x3" in winCheck:
        STATUS = "XWIN"
        break
    elif "x4" in winCheck and "x5" in winCheck and "x6" in winCheck:
        STATUS = "XWIN"
        break
    elif "x7" in winCheck and "x8" in winCheck and "x9" in winCheck:
        STATUS = "XWIN"
        break
    elif "x1" in winCheck and "x4" in winCheck and "x7" in winCheck:
        STATUS = "XWIN"
        break
    elif "x2" in winCheck and "x5" in winCheck and "x8" in winCheck:
        STATUS = "XWIN"
        break
    elif "x3" in winCheck and "x6" in winCheck and "x9" in winCheck:
        STATUS = "XWIN"
        break
    elif "x1" in winCheck and "x5" in winCheck and "x9" in winCheck:
        STATUS = "XWIN"
        break
    elif "x3" in winCheck and "x5" in winCheck and "x7" in winCheck:
        STATUS = "XWIN"
        break
    elif "o1" in winCheck and "o2" in winCheck and "o3" in winCheck:
        STATUS = "OWIN"
        break
    elif "o4" in winCheck and "o5" in winCheck and "o6" in winCheck:
        STATUS = "OWIN"
        break
    elif "o7" in winCheck and "o8" in winCheck and "o9" in winCheck:
        STATUS = "OWIN"
        break
    elif "o1" in winCheck and "o4" in winCheck and "o7" in winCheck:
        STATUS = "OWIN"
        break
    elif "o2" in winCheck and "o5" in winCheck and "o8" in winCheck:
        STATUS = "OWIN"
        break
    elif "o3" in winCheck and "o6" in winCheck and "o9" in winCheck:
        STATUS = "OWIN"
        break
    elif "o1" in winCheck and "o5" in winCheck and "o9" in winCheck:
        STATUS = "OWIN"
        break
    elif "o3" in winCheck and "o5" in winCheck and "o7" in winCheck:
        STATUS = "OWIN"
        break
    if len(Filled) == 9:
        if STATUS != "XWIN" and STATUS != "OWIN":
            STATUS = "DRAW"
    try:
        mouseEntry()
    except GraphicsError:
        win.close()
        break
while True:
    try:
        mouseEntry()
        break
    except:
        win.close()
        break
