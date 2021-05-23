a, b, c, oddNumList = 5, 0, 1, list()
while a != 0:
    b = int(input(" Number " + str(c) + " = "))
    if b % 2 == 1: oddNumList.append(b)
    c, a = c + 1, a - 1
if oddNumList:
    print("Largest Odd Number : " + str(max(oddNumList)))
else:
    print("No odd numbers !")

# a = int(input('How many numbers do u wanna add ? ' ))
# b,c,oddNumList = 0,1,list()
# while (a != 0):
#     b = int(input(" Number " + str(c) + " ? "))
#     if b % 2 == 1: oddNumList.append(b)
#     c,a = c+1,a-1
# if oddNumList != []: print("Largest Odd Number : " + str(max(oddNumList)))
# else: print("No odd numbers !")
