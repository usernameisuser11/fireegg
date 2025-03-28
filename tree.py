base = int(input("입력 진수 결정(16/10/8/2) : "))
numstr = input("값 입력 : ")

if base == 16:
    num = int(numstr, 16)
elif base == 10:
    num = int(numstr, 10)
elif base == 8:
    num = int(numstr, 8)
elif base == 2:
    num = int(numstr, 2)
else:
    print("잘못된 진수 입력입니다.")
    exit()

print(f"16진수 ==> {hex(num)}")
print(f"10진수 ==> {num}")
print(f"8진수 ==> {oct(num)}")
print(f"2진수 ==> {bin(num)}")