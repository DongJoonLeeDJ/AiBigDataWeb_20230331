try:
    a = 10
    b = 2
    print(f"a={a}, b={b}")
    c = a/b
    print(c)
    #exit()
except:
    print("예외!")
    exit() #종료
finally:
    print("어떤 상황이든 꼭 수행")

print("프로그램은 계속 된다.")
