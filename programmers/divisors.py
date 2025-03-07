# 최대 공약수 : 두 수의 약수 중 가장 큰 약수
# 최소 공배수 : 두 수의 배수 중 가장 작은 배수

def solution(n, m):
    answer = []

    # n과 m의 약수 구하기
    n_divisors = [i for i in range(1, n+1) if n % i == 0]
    m_divisors = [i for i in range(1, m+1) if m % i == 0]

    # 최대 공약수 확인하기
    max_divisor = 1

    for n_divisor in n_divisors:
        if (n_divisor in m_divisors) and (max_divisor < n_divisor):
            max_divisor = n_divisor

    answer.append(max_divisor)

    # 최소 공배수 확인하기
    min_multiple = (n // max_divisor) * (m // max_divisor) * max_divisor
    answer.append(min_multiple)

    return answer

print(solution(2, 5))