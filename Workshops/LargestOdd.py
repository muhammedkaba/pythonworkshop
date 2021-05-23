a = input("First Number = ")
b = input("Second Number = ")
c = input("Third Number = ")
a = int(a)
b = int(b)
c = int(c)

d = list()

    
if (a % 2 == 1 or b % 2 == 1 or c % 2 == 1): 
    if a % 2 == 1:
        d.append(a)
    if b % 2 == 1:
        d.append(b)
    if c % 2 == 1:    
        d.append(c)
    d.sort()
    print(d[-1])
else: print("No Odd Numbers")