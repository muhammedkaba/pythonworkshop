b = int(input("uzantı sayısı : "))
a = input("mail adresi : ")


def mailchecker():
    global a, b
    checker = 0
    if "@" not in a:
        return False
    st0 = a.split("@")
    st1 = st0[1].split(".")
    if len(st1) != b:
        return False
    for i in st0[0]:
        check = 0
        for c in list(range(65, 91)) + list(range(97, 123)) + list(range(45, 46)) + list(range(95, 96)):
            if chr(c) == i:
                check = 1
        if check == 1:
            continue
        else:
            checker = 1
    for i in range(b):
        for a in st1[i]:
            check = 0
            for c in list(range(65, 91)) + list(range(97, 123)) + list(range(48, 58)):
                if chr(c) == a:
                    check = 1
            if check == 1:
                continue
            else:
                checker = 1
    if checker == 1:
        return False
    else:
        return True


if not 0 < b < 4:
    print("uzantı sayısı 1 ve 3 arasında olmalıdır.")
else:
    if not mailchecker():
        print("Mail adresiniz yanlıştır.")
    else:
        print("Mail adresiniz doğrudur.")
