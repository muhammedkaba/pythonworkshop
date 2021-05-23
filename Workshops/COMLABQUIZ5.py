dEng = {}
dTur = {}
notFound = []
myList,textList = [],[]
outList = []
wordCount = int(input())
for i in range(wordCount):
    text = input()
    textList = text.split(":")
    dEng[textList[0]] = textList[1]
    dTur[textList[1]] = textList[0]
inputVal = input()
myList = inputVal.split()
if myList[0] == 'TR':
    myList.pop(0)
    myList.sort()
    for i in myList:
        if i in dEng.keys():
            outList.append(i)
        else:
            notFound.append(i)
    outList = list(set(outList))
    outList.sort()
    for a in outList:
        print(a+'='+dEng[a])
if myList[0] == 'EN':
    myList.pop(0)
    myList.sort()
    for i in myList:
        if i in dTur.keys():
            outList.append(i)
        else:
            notFound.append(i)
    outList = list(set(outList))
    outList.sort()
    for a in outList:
        print(a+'='+dTur[a])
if len(notFound) > 0:
    notFound = list(set(notFound))
    notFound.sort()
    print(str(len(notFound))+' word not found: ',end='')
    for i in range(len(notFound)-1):
        print(notFound[i],end=' ')
print(notFound[-1])
