import sys
from pathlib import Path
from collections import deque

filename = Path.cwd() / 'solving-club/input/input_1860.txt'
sys.stdin = open(filename, 'r', encoding='utf-8')

# 진기의 최고급 붕어빵
"""
예약자 : N명
0초 ~ M초의 시간 => K개의 붕어빵
"""
def making_fishbread(arr, m, k):    # arr : 손님들이 오는 시간, m : 붕어빵 만드는데 걸리는 시간,
    # 1초에 몇개 만들 수 있는지
    one_sec = k/m
    # 이전 손님이 왔던 시간
    previous_customer = arr.popleft()
    # 남아있는 붕어빵 개수
    total = 0

    while arr:
        # 첫 번째 손님
        customer = arr.popleft()

        # 첫 번째 손님이 올 때까지 만들 수 있는 붕어빵의 개수
        total += (customer - previous_customer) * one_sec_num

        # 가장 빨리오는 손님이 붕어빵을 먹을 수 있다면
        if total < 1:
            return 'Impossible'

        total -= 1
        previous_customer = customer

    return 'possible'


# 테스트 케이스 수
T = int(input())

for tc in range(1, T+1):
    # 예약 손님 수, K개 만드는 데 걸리는 시간, M초 동안 만들 수 있는 붕어빵 개수
    N, M, K = map(int, input().split())

    # 예약 손님 도착 시간
    seconds = list(map(int, input().split()))
    # 정렬
    for i in range(0, N-1):
        for j in range(i, N):
            if seconds[i] > seconds[j]:
                seconds[i], seconds[j] = seconds[j], seconds[i]

    seconds = deque(seconds)    # 덱으로 만든다.

    # 붕어빵 만들기 시작
    answer = making_fishbread(seconds, M, K)

    print(f'#{tc} {answer}')