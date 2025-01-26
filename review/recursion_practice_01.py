# 1부터 n까지의 합 구하기
def add_from_n_to_one(n):
    # 1보다 작거나 같으면 1 반환
    if n <= 1:
        return 1
    # 1보다 크면 해당 숫자(n)와 해당 숫자에서 하나 작은 숫자를 넣은 함수(func(n-1)) 더하기
    else:
        return n + add_from_n_to_one(n-1)
    
    
print(add_from_n_to_one(10))