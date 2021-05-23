text = input()
combinedText = ''
myList = []
for letter in text:
    myList.append(letter)
for i in range(len(myList)):
    for check1 in range(65,78):
        if chr(check1) == myList[i]:
            myList[i] = str(chr(check1-7))
            break
    for check1 in range(78,91):
        if chr(check1) == myList[i]:
            myList[i] = str(chr(check1+2))
            break
    for check1 in range(97,110):
        if chr(check1) == myList[i]:
            myList[i] = str(chr(check1-4))
            break
    for check1 in range(110,123):
        if chr(check1) == myList[i]:
            myList[i] = str(chr(check1+6))
            break
for combinec in myList:
    combinedText += str(combinec)
print(combinedText)
text2 = input()
combinedText2 = ''
myList2 = []
for letter in text2:
    myList2.append(letter)
for i in range(len(myList2)):
    for check1 in range(58,78):
        if chr(check1) == myList2[i]:
            myList2[i] = str(chr(check1+7))
            break
    for check1 in range(78,93):
        if chr(check1) == myList2[i]:
            myList2[i] = str(chr(check1-2))
            break
    for check1 in range(93,110):
        if chr(check1) == myList2[i]:
            myList2[i] = str(chr(check1+4))
            break
    for check1 in range(110,129):
        if chr(check1) == myList2[i]:
            myList2[i] = str(chr(check1-6))
            break

for combinec in myList2:
    combinedText2 += str(combinec)
print(combinedText2)
