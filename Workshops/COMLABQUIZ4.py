in1, in2, in3 = input().split()
student = int(in1)
labCount = int(in2)
hwCount = int(in3)
ifAnyCheck = 0
myDict = {}
labSum, hwSum = 0, 0
for i in range(student):
    myDict["students{0}".format(i)] = input().split()
sidNos = input().split()
for i in sidNos:
    for a in range(student):
        if myDict["students{0}".format(a)][0] == i:
            ifAnyCheck = 1
            labG = [0]
            hwG = [0]
            midtG = 0
            finalG = 0
            counter = 0
            checker = 0
            labSum = 0
            hwSum = 0
            for x in myDict["students{0}".format(a)]:
                if x == '>':
                    counter += 1
                    checker = 0
                if checker == 1:
                    if counter == 0:
                        labG.append(x)
                    if counter == 1:
                        hwG.append(x)
                    if counter == 2:
                        midtG = x
                    if counter == 3:
                        finalG = x
                if x == '<':
                    checker = 1
            for y in range(len(labG)):
                labSum += int(labG[y])
            for z in range(len(hwG)):
                hwSum += int(hwG[z])
            labAv = labSum / labCount
            hwAv = hwSum / hwCount
            avNo = labAv / 10 + hwAv / 10 + int(midtG) / 10 + int(finalG) * 8 / 10
            print(myDict["students{0}".format(a)][1] + ' ' + myDict["students{0}".format(a)][2] + ' ' + "{:.2f}".format(
                avNo))
if ifAnyCheck == 0:
    print("None")
