# 배열 연습문제1
"""
N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이 출력

[입력]
- 첫 줄에 테스트 케이스의 수 T가 주어진다. (1 <= T <= 50)
- 각 케이스의 첫 줄에 양수의 개수 N이 주어진다. (5 <= N <= 1000)
- 다음 줄에 N개의 양수 ai가 주어진다. (1 <= ai <= 1000000)

[출력]
- 각 줄마다 '#T' (T는 테스트 케이스 번호)를 출력한 뒤, 빈칸에 이어 답을 출력
"""

def max_minus_min(arr, n):
    # 최소일 것 같은, 최대일 것 같은 인덱스 설정
    min_idx, max_idx = 0, 0
    
    for i in range(1, n):
        if arr[i] < arr[min_idx]:
            min_idx = i
        
        if arr[i] > arr[max_idx]:
            max_idx = i
            
    return arr[max_idx] - arr[min_idx]
    


T = int(input())

for test_case in range(1, T+1):
    # 양수 N
    N = int(input())
    # N개의 양수 ai
    a = list(map(int, input().split()))
    
    result = max_minus_min(a, N)
    
    print(f'#{test_case} {result}')