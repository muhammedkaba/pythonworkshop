import math

intCheck = False
# circleCount = 2
circleCount = int(input())
myDict = {}
sumofRect = 0
myList = []
# myDict["circles0"] = '40 10 10'.split()
# myDict["circles1"] = '40 20 10'.split()
for i in range(circleCount):
    myDict["circles{0}".format(i)] = input().split()
for x in range(circleCount):
    cr1x = int(myDict["circles{0}".format(x)][0])
    cr1y = int(myDict["circles{0}".format(x)][1])
    cr1r = int(myDict["circles{0}".format(x)][2])
    cr1maxx = cr1x + cr1r
    cr1minx = cr1x - cr1r
    cr1maxy = cr1y + cr1r
    cr1miny = cr1y - cr1r
    intCheck = False
    print('('+' '+str(cr1x)+' '+str(cr1y)+' '+') '+'rad: '+str(cr1r))
    if x in myList:
        continue
    for a in range(circleCount):
        cr2x = int(myDict["circles{0}".format(a)][0])
        cr2y = int(myDict["circles{0}".format(a)][1])
        cr2r = int(myDict["circles{0}".format(a)][2])
        cr2maxx = cr2x + cr2r
        cr2minx = cr2x - cr2r
        cr2maxy = cr2y + cr2r
        cr2miny = cr2y - cr2r
        dsq = (cr1x-cr2x)**2 + (cr1y-cr2y)**2
        d = math.sqrt(dsq)
        if cr1r+cr2r > d:
            intCheck = True
        if a == x:
            intCheck = False
        if intCheck:
            myList.append(a)
            if cr2maxx < cr1maxx:
                maxX = cr1maxx
            else:
                maxX = cr2maxx
            if cr2maxy < cr1maxy:
                maxY = cr1maxy
            else:
                maxY = cr2maxy
            if cr2minx < cr1minx:
                minX = cr2minx
            else:
                minX = cr1minx
            if cr2miny < cr1miny:
                minY = cr2miny
            else:
                minY = cr1miny
            sumofRect += ((maxX-minX)*(maxY-minY))
            break
    if not intCheck:
        sumofRect += ((cr1maxx-cr1minx)*(cr1maxy-cr1miny))
print('Total rect area: '+str(sumofRect))
