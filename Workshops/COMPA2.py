from graphics import *

win = GraphWin("Calculator", 600, 600)
STATUS = "START"
inputText = ""
operator = ""
var1, var2 = 0, 0
a = Point(0, 0)
aX, aY = a.getX(), a.getY()
# LINES
yLine1 = Line(Point(150, 100), Point(150, 500))
yLine2 = Line(Point(300, 100), Point(300, 600))
yLine3 = Line(Point(450, 100), Point(450, 600))
xLine1 = Line(Point(0, 100), Point(600, 100))
xLine2 = Line(Point(0, 200), Point(600, 200))
xLine3 = Line(Point(0, 300), Point(600, 300))
xLine4 = Line(Point(0, 400), Point(600, 400))
xLine5 = Line(Point(0, 500), Point(600, 500))
# TEXTS
textAC = Text(Point(75, 150), "AC")
textPM = Text(Point(225, 150), "+/-")
textRM = Text(Point(375, 150), "%")
textDT = Text(Point(525, 150), "/")
text7 = Text(Point(75, 250), "7")
text8 = Text(Point(225, 250), "8")
text9 = Text(Point(375, 250), "9")
textML = Text(Point(525, 250), "*")
text4 = Text(Point(75, 350), "4")
text5 = Text(Point(225, 350), "5")
text6 = Text(Point(375, 350), "6")
textSB = Text(Point(525, 350), "-")
text1 = Text(Point(75, 450), "1")
text2 = Text(Point(225, 450), "2")
text3 = Text(Point(375, 450), "3")
textPL = Text(Point(525, 450), "+")
text0 = Text(Point(150, 550), "0")
textPO = Text(Point(375, 550), "**")
textEQ = Text(Point(525, 550), "=")
myList = [yLine1, yLine2, yLine3, xLine1, xLine2, xLine3, xLine4, xLine5, textAC, textPM, textRM, textDT, text7, text8,
          text9, textML, text4, text5, text6, textSB, text1, text2, text3, textPL, text0, textPO, textEQ]
for i in myList:
    i.draw(win)


def var1var2():
    global var1, var2
    inputBox.setText(inputText)
    var1 = inputBox.getText()


def setTextSt():
    global STATUS
    inputBox.setText(inputText)
    STATUS = "A"


def operatorNotF():
    global STATUS, inputText, operator, var1, var2
    inputText = ""
    var2 = inputBox.getText()
    if operator == "+":
        inputText = str(int(var1) + int(var2))
        var1var2()
    if operator == "-":
        inputText = str(int(var1) - int(var2))
        var1var2()
    if operator == "*":
        inputText = str(int(var1) * int(var2))
        var1var2()
    if operator == "/":
        if int(var1) / int(var2) % 1 == 0:
            inputText = str(int(int(var1) / int(var2)))
            var1var2()
        else:
            inputText = str(int(var1) / int(var2))
            var1var2()
    if operator == "%":
        inputText = str(int(var1) % int(var2))
        var1var2()
    if operator == "**":
        inputText = str(int(var1) ** int(var2))
        var1var2()


def mouseButtonSt():
    global STATUS, inputText, operator, var1, var2, a, aX, aY
    a = win.getMouse()
    aX = a.getX()
    aY = a.getY()
    if 0 < aX < 150 and 400 < aY < 500:  # 1
        inputText = "1"
        setTextSt()
    if 150 < aX < 300 and 400 < aY < 500:  # 2
        inputText = "2"
        setTextSt()
    if 300 < aX < 450 and 400 < aY < 500:  # 3
        inputText = "3"
        setTextSt()
    if 0 < aX < 150 and 300 < aY < 400:  # 4
        inputText = "4"
        setTextSt()
    if 150 < aX < 300 and 300 < aY < 400:  # 5
        inputText = "5"
        setTextSt()
    if 300 < aX < 450 and 300 < aY < 400:  # 6
        inputText = "6"
        setTextSt()
    if 0 < aX < 150 and 200 < aY < 300:  # 7
        inputText = "7"
        setTextSt()
    if 150 < aX < 300 and 200 < aY < 300:  # 8
        inputText = "8"
        setTextSt()
    if 300 < aX < 450 and 200 < aY < 300:  # 9
        inputText = "9"
        setTextSt()
    if 0 < aX < 150 and 100 < aY < 200:  # AC
        STATUS = "START"


def mouseButtonAC():
    global STATUS, inputText, operator, var1, var2, a, aX, aY
    a = win.getMouse()
    aX = a.getX()
    aY = a.getY()
    ops()
    if 0 < aX < 150 and 400 < aY < 500:  # 1
        inputText += "1"
        setTextSt()
    if 150 < aX < 300 and 400 < aY < 500:  # 2
        inputText += "2"
        setTextSt()
    if 300 < aX < 450 and 400 < aY < 500:  # 3
        inputText += "3"
        setTextSt()
    if 0 < aX < 150 and 300 < aY < 400:  # 4
        inputText += "4"
        setTextSt()
    if 150 < aX < 300 and 300 < aY < 400:  # 5
        inputText += "5"
        setTextSt()
    if 300 < aX < 450 and 300 < aY < 400:  # 6
        inputText += "6"
        setTextSt()
    if 0 < aX < 150 and 200 < aY < 300:  # 7
        inputText += "7"
        setTextSt()
    if 150 < aX < 300 and 200 < aY < 300:  # 8
        inputText += "8"
        setTextSt()
    if 300 < aX < 450 and 200 < aY < 300:  # 9
        inputText += "9"
        setTextSt()
    if 0 < aX < 300 and 500 < aY < 600:  # 0
        inputText += "0"
        setTextSt()
    minus()


def opsMin():
    global STATUS, inputText, operator, var1, var2, a, aX, aY
    var1 = inputBox.getText()
    STATUS = "B"
    inputText = ""


def ops():
    global STATUS, inputText, operator, var1, var2, a, aX, aY
    if 0 < aX < 150 and 100 < aY < 200:  # AC
        STATUS = "START"
    if 300 < aX < 450 and 100 < aY < 200:  # %
        if operator != "":
            operatorNotF()
            operator = "%"
            STATUS = "B"
        else:
            opsMin()
            operator = "%"
    if 450 < aX < 600 and 100 < aY < 200:  # /
        if operator != "":
            try:
                operatorNotF()
                STATUS = "B"
                operator = "/"
            except:
                STATUS = "START"
        else:
            opsMin()
            operator = "/"
    if 450 < aX < 600 and 200 < aY < 300:  # *
        if operator != "":
            operatorNotF()
            STATUS = "B"
            operator = "*"
        else:
            opsMin()
            operator = "*"
    if 450 < aX < 600 and 300 < aY < 400:  # -
        if operator != "":
            operatorNotF()
            STATUS = "B"
            operator = "-"
        else:
            opsMin()
            operator = "-"
    if 450 < aX < 600 and 400 < aY < 500:  # +
        if operator != "":
            operatorNotF()
            STATUS = "B"
            operator = "+"
        else:
            opsMin()
            operator = "+"
    if 300 < aX < 450 and 500 < aY < 600:  # **
        if operator != "":
            operatorNotF()
            STATUS = "B"
            operator = "**"
        else:
            opsMin()
            operator = "**"


def minus():
    global STATUS, inputText, operator, var1, var2, a, aX, aY
    if 150 < aX < 300 and 100 < aY < 200:  # +/-
        STATUS = "C"
        if "." in inputText:
            inputText = str(-float(inputText))
            inputBox.setText(inputText)
        else:
            inputText = str(-int(inputText))
            inputBox.setText(inputText)


def eq():
    global STATUS, inputText, operator, var1, var2, a, aX, aY
    if 450 < aX < 600 and 500 < aY < 600:  # =
        STATUS = "D"
        if operator != "":
            try:
                operatorNotF()
                STATUS = "D"
                operator = ""
            except:
                STATUS = "START"


inputBox = Entry(Point(300, 50), 20)
inputBox.draw(win)


def MouseEntry():
    global STATUS, inputText, operator, var1, var2, a, aX, aY
    if STATUS == "START":
        inputText = "0"
        operator = ""
        var1, var2 = 0, 0
        inputBox.setText(inputText)
        mouseButtonSt()
    elif STATUS == "A":
        mouseButtonAC()
        eq()
    elif STATUS == "B":
        mouseButtonSt()
        if (0 < aX < 600 and 100 < aY < 200) or (450 < aX < 600 and 100 < aY < 600) or (
                300 < aX < 450 and 500 < aY < 600):
            STATUS = "START"
        if 0 < aX < 300 and 500 < aY < 600:  # 0
            inputText += "0"
            setTextSt()
    elif STATUS == "C":
        mouseButtonAC()
        eq()
    elif STATUS == "D":
        a = win.getMouse()
        aX = a.getX()
        aY = a.getY()
        ops()
        minus()
        if (0 < aX < 450 and 200 < aY < 500) or (0 < aX < 300 and 500 < aY < 600):
            STATUS = "START"


while True:
    try:
        MouseEntry()
    except GraphicsError:
        win.close()
        break
