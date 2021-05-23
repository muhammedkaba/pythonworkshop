myList0 = []
myList1 = []
for i in range(7):
    a = int(input("{0}".format(i+1)+". Sayı = "))
    if a == 0:
        myList0.append(a)
    else:
        myList1.append(a)
print(myList0+myList1)
