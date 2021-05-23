divisorCount = 0
sumOfPrimNums = 0
while True:
    a = int(input())
    if a > 0:
        for i in range(1, a):
            if a % i == 0:
                divisorCount += 1
        if divisorCount == 1:
            sumOfPrimNums += a
        divisorCount = 0
    if a < 0:
        break
print(sumOfPrimNums)
