a = 1;
for i in range(365):
    print(i+1, end=" => ")
    a = a+(a*(1/100))
    print(a)