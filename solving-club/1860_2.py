import sys
from pathlib import Path
from collections import deque

filename = Path.cwd() / 'solving-club/input/input_1860_2.txt'
sys.stdin = open(filename, 'r', encoding='utf-8')

# 진기의 최고급 붕어빵
"""
예약자 : N명
0초 ~ M초의 시간 => K개의 붕어빵 (한번에)
"""
def make_fishbread(arr, people, m, k):
    result = 'Possible'
    
    while arr:
        current = arr.popleft()    # 디큐
        
        total_bread = (current // m) * k    # 현재 시간까지 만든 총 붕어빵의 개수
        total_bread -= people    # 현재 남아있는 붕어빵 개수
        
        if total_bread <= 0:    # 방문한 사람 수 보다 현재까지 만든 붕어빵의 개수가 더 적으면
            result = 'Impossible'
            break
        
        people += 1
        
    return result


# 테스트 케이스 수
T = int(input())

for tc in range(1, T+1):
    
    # 예약 손님 수, K개 만드는 데 걸리는 시간, M초 동안 만들 수 있는 붕어빵 개수
    N, M, K = map(int, input().split())

    # 예약 손님 도착 시간
    seconds = list(map(int, input().split()))
    
    # 오름차순 정렬
    for i in range(0, N-1):
        for j in range(i, N):
            if seconds[i] > seconds[j]:
                seconds[i], seconds[j] = seconds[j], seconds[i]
                
    seconds = deque(seconds)    # 덱으로 만들기
    
    # 첫 번째 손님이 왔던 시간 비교
    first = seconds.popleft()    # 디큐
    
    if first < M:    # 만약 첫 손님이 처음 만들어지는 시간보다 일찍 오면
        answer = 'Impossible'    # 불가능
        
    else:    # 처음 만들어지는 시간과 같거나 늦게 오면
        total_people = 1
        answer = make_fishbread(seconds, total_people, M, K)
        
    print(f'#{tc} {answer}')