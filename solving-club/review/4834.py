import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_4834.txt'
sys.stdin = open(filename, 'r')

"""
- 0~9 까지 숫자가 적힌 N장의 카드
- 가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력
- 카드 장수가 같을 때는 적힌 숫자가 큰 쪽 선택
"""


def max_cards(arr, n=10):
    max_idx = 0
    for i in range(1, n):
        # max
        if arr[max_idx] <= arr[i]:
            max_idx = i

    return max_idx, arr[max_idx]


# 테스트 케이스 개수
T = int(input())

for test_case in range(1, T+1):
    # 카드 장수
    N = int(input())
    # 카드
    a = int(input())
    # temp
    temp = [0] * 10

    for _ in range(N):
        temp[a % 10] += 1
        a //= 10

    card_num, cnt = max_cards(temp)

    print(f'#{test_case} {card_num} {cnt}')