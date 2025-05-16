inFp = None
inList, inStr = [], ""

inFp = open("C:/Temp/data.txt", "r", encoding="utf-8")
inList = inFp.readlines()

for i in range(len(inList)):
    print(str(i + 1) + ". " + inList[i], end="")

inFp.close()
