import sys
from pathlib import Path
from collections import deque

filename = Path.cwd() / 'solving-club/input/input_1860_2.txt'
sys.stdin = open(filename, 'r', encoding='utf-8')

# 진기의 최고급 붕어빵
"""
예약자 : N명
0초 ~ M초의 시간 => K개의 붕어빵
"""
def making_fishbread(arr, in_one):    # arr : 손님들이 오는 시간,
    fishes = [0] * 11112
    previous = 0
    pre_total = 0

    while arr:
        customer = arr.popleft()    # 손님 도착 시간

        for sec in range(previous+1, customer+1):    # 손님 도착 시간까지의 붕어빵 넣어줌.
            fishes[sec] = in_one

        total = sum(fishes) + pre_total

        if total >= 1:    # 붕어빵이 적어도 하나는 있음.
            total -= 1    # 붕어빵 하나 주기
        else:
            return 'Impossible'

        # 다음 손님 확인을 위한 업데이트
        previous = customer
        pre_total = total

    return 'Possible'


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

    one_sec = K/M

    answer = making_fishbread(seconds, one_sec)

    print(f'#{tc} {answer}')