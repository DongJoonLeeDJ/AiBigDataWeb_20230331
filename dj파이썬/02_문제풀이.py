print("ù��° ���� �Է��ϼ���.")
num1 = input()
num2 = input("�ι�° ���� �Է��ϼ���.")
print(int(num1) * int(num2))

#1 ���ڿ�,�ε��� ������ �� ���
print(int(num1) * int(num2[2]))
print(int(num1) * int(num2[1]))
print(int(num1) * int(num2[0]))

#2 �������� ������ �������� ó���� ���
print(int(num1) *  (int(num2)%10) )
print(int(num1) * ((int(num2)//10)%10))
print(int(num1) * (int(num2)//100))