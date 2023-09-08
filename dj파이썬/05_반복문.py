count = 0
while count<100:
    count += 1
    print(f"count={count}")
print(f"count={count}")

count = 0
while count<100:
    count+=1
    if count%2==0:
        continue
    if count>50:
        break
    print("count="+str(count))
print("반복문 끝!")

#range : 범위
#1이상 11미만
for item in range(1,11):
    print(item)

for item in range(1,6):
    print("*"*item)

sum = 0
for item in range(1,101):
    if item%2==1:
        continue
    sum += item
print(f"sum={sum}(1부터 100까지의 합 중 짝수만 더한 거)")

students = [('이동준','남성'),('이유나','여성'),('정민욱','남성'),('박명회','남성')]
for a,b in students:
    print(f"이름:{a}, 성별:{b}")

students = [('이동준','남성',34),('이유나','여성',20),('박명회','남성',40)]
for a,b,c in students:
    print(f"이름:{a}, 성별:{b}, 나이:{c}")


dj = {
    'name' : '이동준',
    'born' : '19890430',
    'gen' : '남'
}

for item in dj.items():
    print(item) #튜플 형태로 출력함
for key,value in dj.items():
    print(f"속성:{key}, 값:{value}")