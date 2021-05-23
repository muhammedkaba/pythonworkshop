inputs1 = input().split()
inputs2 = input().split()
b = 0
d = 0
myList = []
for a in range(0, len(inputs1)):
    for i in range(0, len(inputs2)):
        if inputs2[i] in inputs1[a]:
            c = 0
            myList = []
            b = inputs1[a].count(inputs2[i])
            for x in range(0, b):
                if x == 0:
                    c = inputs1[a][c + x:].index(inputs2[i])
                    myList.append(c + x)
                if x > 0:
                    d = c
                    c = inputs1[a][c + x:].index(inputs2[i])
                    myList.append(c + d + x)
            print(inputs1[a] + " " + inputs2[i] + " " + str(b) + " " + str(myList))
