age = 34
print("����� ���̴� " + str(age) + "���Դϴ�.")
print(f"����� ���̴� {age}�Դϴ�.")
print("����� ���̴� {}���Դϴ�.".format(age))
print("����� ���̴� %d���Դϴ�." % age)

year = int(input("�¾ ������ �Է��ϼ���."))
year = year % 12

if year==9:
    print("��")
elif year==10:
    print("��")
elif year==11:
    print("��")
elif year==0:
    print("������")
elif year==1:
    print("��")
elif year==2:
    print("��")
elif year==3:
    print("����")
elif year==4:
    print("��")
elif year==5:
    print("��")
elif year==6:
    print("ȣ����")
elif year==7:
    print("�䳢")
elif year==8:
#else:
    print("��")