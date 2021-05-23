a = 0
b = input("bir liste giriniz : ")
for i in list(b.split(",")):
    if int(i) % 2 != 0 and int(i) > a:
        a = int(i)
print(a)
