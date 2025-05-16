inFp = None
inStr = ""
lineNumber = 1  

inFp = open("c:\\users\\tutor\\Downloads\\python실습\\.dist\\FileTest\\d", encoding="utf-8")
while True:
    inStr = inFp.readline()
    if inStr == "":
        break
    print(f"{lineNumber}. {inStr}", end="")  
    lineNumber += 1  

inFp.close()
