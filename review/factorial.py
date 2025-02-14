# for문 사용하기
def factorial(number):
    total = 1
    for n in range(1, number+1):
        total *= n
    return total


print(factorial(5))


# 재귀 호출 사용하기
def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number-1)
    

print(factorial(5))