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
print("�ݺ��� ��!")

#range : ����
#1�̻� 11�̸�
for item in range(1,11):
    print(item)

for item in range(1,6):
    print("*"*item)

sum = 0
for item in range(1,101):
    if item%2==1:
        continue
    sum += item
print(f"sum={sum}(1���� 100������ �� �� ¦���� ���� ��)")

students = [('�̵���','����'),('������','����'),('���ο�','����'),('�ڸ�ȸ','����')]
for a,b in students:
    print(f"�̸�:{a}, ����:{b}")

students = [('�̵���','����',34),('������','����',20),('�ڸ�ȸ','����',40)]
for a,b,c in students:
    print(f"�̸�:{a}, ����:{b}, ����:{c}")


dj = {
    'name' : '�̵���',
    'born' : '19890430',
    'gen' : '��'
}

for item in dj.items():
    print(item) #Ʃ�� ���·� �����
for key,value in dj.items():
    print(f"�Ӽ�:{key}, ��:{value}")