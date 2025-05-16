inFp, outFp = None, None
inStr = ""

inFileName = input("읽을 파일명 입력 (예: C:/Windows/win.ini) : ")
outFileName = input("저장할 파일명 입력 (예: C:/Temp/data3.txt) : ")

inFp = open(inFileName, "r", encoding="utf-8")
outFp = open(outFileName, "w", encoding="utf-8")

inList = inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print(f"---'{inFileName}' 파일을 '{outFileName}'(으)로 정상적으로 복사했음---")

