print("첫번째 숫자 입력하세요.")
num1 = input()
num2 = input("두번째 숫자 입력하세요.")
print(int(num1) * int(num2))

#1 문자열,인덱스 개념을 알 경우
print(int(num1) * int(num2[2]))
print(int(num1) * int(num2[1]))
print(int(num1) * int(num2[0]))

#2 나눗셈과 나머지 연산으로 처리할 경우
print(int(num1) *  (int(num2)%10) )
print(int(num1) * ((int(num2)//10)%10))
print(int(num1) * (int(num2)//100))