nbumbeer_ri = int(input("1.입력한 수식 계산, 2.두 수 사이의 합계:"))
if nbumbeer_ri == 1 :
    expression = input("***수식을 입력하세요")
    answer = eval(expression) 
    print(expression,'결과는', answer ,'입니다.')
elif nbumbeer_ri == 2 :
     a=int(input("첫 번째 숫자를 입력학세요."))
     b=int(input("두 번째 숫자를 입력하세요."))
     count_between_numbers = abs(a-b)+1
     total = (a+b) * count_between_numbers /2
     print(f"{a}와 {b} 사이의 합은 {total}입니다.")
