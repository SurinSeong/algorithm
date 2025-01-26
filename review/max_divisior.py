# 두 자연수 a, b의 최대 공약수 구하기
# 두 수의 약수 중 공통된 것을 찾아 그 중 최대인 것을 찾기
# 1. 재귀 호출 이용하기
# 1) 두 수 중 더 작은 값을 최대 공약수 후보로 설정
# 2) 최대 공약수 후보를 계속 감소 시키며 최대 공약수를 찾는다.
def find_max_divisor(num1, num2):
    # 둘 중 더 작은 값 찾기
    min_number = min(num1, num2)
    # 공약수 후보가 두 수를 다 딱 떨어지게 나눌 수 있다면 최대공약수로 확정
    while True:
        if (num1 % min_number == 0) & (num2 % min_number == 0):
            return min_number
        else:
            min_number -= 1
        
    

print(find_max_divisor(10, 6))


# 유클리드가 발견한 최대공약수의 성질
# a, b의 최대 공약수는 b와 a를 b로 나눈 나머지의 최대공약수과 같다.
# gcd(a, b) = gcd(b, a%b)
# 어떤 수와 0의 최대 공약수는 자기 자신이다. gcd(n, 0) = n
def find_max_divisor(num1, num2):
    if num1 * num2 == 0:
        return abs(num1 + num2)
    else:
        return find_max_divisor(num2, num1%num2)
    
    
print(find_max_divisor(10, 6))