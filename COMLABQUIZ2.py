inputs = map(str, input().split())

isString = False
isFloat = False
sumOfIntegers = 0
sumOfFloats = 0
sumOfStrings = ""
floatThere = False
intThere = False
stringThere = False
for b in inputs:
    if chr(46) in b:
        sumOfFloats += float(b)
        isFloat = True
        floatThere = True
    if not isFloat:
        for i in range(65, 91):
            if chr(i) in b:
                sumOfStrings += b
                isString = True
                stringThere = True
                break
        if not isString:
            for d in range(97, 123):
                if chr(d) in b:
                    sumOfStrings += b
                    stringThere = True
                    isString = True
                    break
        if not isString:
            for d in range(33, 48):
                if chr(d) in b:
                    sumOfStrings += b
                    stringThere = True
                    isString = True
                    break
        if not isString:
            for d in range(58, 65):
                if chr(d) in b:
                    sumOfStrings += b
                    stringThere = True
                    isString = True
                    break

    if not isString:
        if not isFloat:
            sumOfIntegers += int(b)
            intThere = True
    isString = False
    isFloat = False

if intThere:
    print(sumOfIntegers)
if floatThere:
    print(sumOfFloats)
if stringThere:
    print(sumOfStrings)
