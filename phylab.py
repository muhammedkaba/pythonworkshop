import math
x = int(input("How many numbers do u have ? "))
y,c = float(x),x
myList = []
listSum,squareSum,sumAbs,normDev,z = 0,0,0,0,0
while (x != 0):
    x = x-1
    a = float(input("Numbers "))
    myList.append(a) 
while (c != 0):
    listSum = math.fsum(myList)
    c = c-1
    arMean = (listSum/y)
while (z != y):
    squareSum = (squareSum + ((arMean-myList[z])**2))
    sumAbs = (sumAbs + (abs(arMean-myList[z])))
    normDev = (-(arMean-myList[z]))
    print(normDev)
    z = z+1
stDev =  (math.sqrt(squareSum/(y-1)))
avDev = (sumAbs/y)

print("Standard Deviation = ",stDev)
print("Arithmetic Mean = ",arMean)
print("Varians = ",stDev**2)
print("Average Deviation = ",avDev)
