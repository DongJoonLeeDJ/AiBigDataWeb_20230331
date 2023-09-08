myinfo = True
"""
1. 조건 끝에 콜론(:)이 반드시 붙음
2. 조건 밑에 반드시 들여쓰기 4칸을 해줘야 함(혹은 tab)
* 들여쓰기 4칸이 권장 사항
"""
if myinfo:
    print("이 정보는 사실입니다.")

age = 30
if age>20:
    print('성인입니다.')

#if age>0 and age<30:
if age > 0 & age < 30:
    print("1~29살입니다.")

if age>0 or age<100: #or 대신에 | (shift + \)
    print('일반적인 나이입니다.')