# 구간합
def add_around(arr, n, m):
    max_sum, min_sum = float('-inf'), float('inf')
    
    for i in range(0, n-m+1):
        current_sum = 0
        for k in range(m):
            current_sum += arr[i+k]
        
        if max_sum < current_sum:
            max_sum = current_sum
            
        if min_sum > current_sum:
            min_sum = current_sum
    
    return max_sum - min_sum


T = int(input())

for test_case in range(1, T+1):
    
    # 정수의 개수, 구간의 개수
    N, M = map(int, input().split())
    
    # 정수 리스트
    a = list(map(int, input().split()))
    
    result = add_around(a, N, M)
    
    print(f'#{test_case} {result}')