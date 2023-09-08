print("-"*50)
"""
여러 줄 짜리 주석
multi command line
Hello
"""
a = """
안녕하세요.
이동준입니다.
Python 처음은 아니지만 잘 부탁해요.
"""
print(a)

mylist = [1,2,3,4,5]
print(mylist[-1]) # 5 (음수 인덱스)
print(mylist[-2]) # 4
print(mylist[1:4]) # 2, 3, 4 (슬라이싱)

print("안녕하세요"[0]) #안
print("안녕하세요"[-1]) #요

a = 'Hello' + ' World'
print(a)
b = 'Hey ' + '1989'
print(b)
c = 1989
d = 'Hello ' + str(c) #숫자는 문자열로 변환을 해줘야 + 연산이 먹힘
print(d)
e = int('1989') + 1
print(e)












