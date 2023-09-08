numbers = list(range(1,11)) #[1,2,3,4,5,6,7,8,9,10]
print(numbers)

def isOdd(n):
    return n%2!=0

oddlist = list(filter(isOdd,range(1,11)))
print(oddlist)
# lambda x:x%2!=0 -> 콜백함수
# 콜백함수 : 함수의 매개변수가 되는 함수
oddlist = list(filter(lambda x:x%2!=0, range(1,11)))
print(oddlist)

nums = range(1,6)
powerList = list(map(lambda x:x**3, nums))
print(powerList)
powerFunc = lambda x:x**3
def mypower(x):
    return x**3
powerList = list(map(powerFunc, nums))
print(powerList)
powerList = list(map(mypower, nums))
print(powerList)
