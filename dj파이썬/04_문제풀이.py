age = 34
print("당신의 나이는 " + str(age) + "살입니다.")
print(f"당신의 나이는 {age}입니다.")
print("당신의 나이는 {}살입니다.".format(age))
print("당신의 나이는 %d살입니다." % age)

year = int(input("태어난 연도를 입력하세요."))
year = year % 12

if year==9:
    print("뱀")
elif year==10:
    print("말")
elif year==11:
    print("양")
elif year==0:
    print("원숭이")
elif year==1:
    print("닭")
elif year==2:
    print("개")
elif year==3:
    print("돼지")
elif year==4:
    print("쥐")
elif year==5:
    print("소")
elif year==6:
    print("호랑이")
elif year==7:
    print("토끼")
elif year==8:
#else:
    print("용")