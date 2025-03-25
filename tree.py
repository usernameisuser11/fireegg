base = int(input("입력 진수 (16/10/8/2): "))
num = int(input("숫자 입력: "), base)
print(f"16진수==>{hex(num)}, 10진수==>{num}, 8진수==>{oct(num)}, 2진수==>{bin(num)}")
