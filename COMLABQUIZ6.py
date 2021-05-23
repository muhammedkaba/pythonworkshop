class ListClass:
    def __init__(self, List,listname):
        self.list = List
        self.listname = listname
    def printName(self):
        print("Name: "+self.listname)
    def __str__(self):
        outList = ''
        for i in self.list:
            outList = outList + str(i) + ' '
        return '[' + outList[:-1] + ']'
    def getLength(self):
        return len(self.list)
    def printOdds(self):
        Out = ''
        for i in self.list:
            if i % 2 == 1:
                Out += str(i) + ' '
        print(Out[:-1])
    def printEvens(self):
        Out = ''
        for i in self.list:
            if i % 2 == 0:
                Out += str(i) + ' '
        print(Out[:-1])
    def changeItem(self,old,new):
        for i in range(len(self.list)):
            if self.list[i] == old:
                self.list[i] = new
    def addItem(self,var):
        a = False
        for i in range(len(self.list)):
            if self.list[i] == var:
                a = True
        if a == False:
            self.list.append(var)
    def addItems(self,Vars):
        for i in Vars:
            b = True
            for a in range(len(self.list)):
                if self.list[a] == i:
                    b = False
            if b == True:
                self.list.append(i)
    def removeItem(self,var):
        a = False
        for i in range(len(self.list)):
            if self.list[i] == var:
                a = True
        if a == True:
            self.list.remove(var)
    def removeItems(self,Vars):
        for i in Vars:
            b = False
            for a in range(len(self.list)):
                if self.list[a] == i:
                    b = True
            if b == True:
                self.list.remove(i)
    def __lt__(self,other):
        selfSum = 0
        otherSum = 0
        for i in self.list:
            selfSum += i
        for i in other.list:
            otherSum += i
        return selfSum < otherSum