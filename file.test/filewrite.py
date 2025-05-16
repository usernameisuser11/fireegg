outFp = None
outStr = ""

fileName = input("저장할 파일명 입력 (예: C:/Temp/data2.txt) : ")
outFp = open(fileName, "w", encoding="utf-8")  # 파일명 입력받아서 사용

while True:
    outStr = input("내용 입력 : ")
    if outStr != "":
        outFp.writelines(outStr + "\n")
    else:
        break

outFp.close()
print(f"---정상적으로 '{fileName}' 파일에 씀---")
