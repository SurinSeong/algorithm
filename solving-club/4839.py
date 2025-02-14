# 이진 탐색
# A, B에게 찾을 번호를 알려줌.
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_4839.txt'
sys.stdin = open(filename, 'r')


# 함수
def find_page(pages, right):
    left = 1
    try_number = 0
    while left < right:
        center = int((left + right) / 2)
        # 찾는 횟수
        try_number += 1
        if center < pages:
            left = center + 1
        elif center > pages:
            right = center - 1
        else:
            break

    return try_number


# 테스트 케이스 개수
T = int(input())

for t in range(1, T+1):
    # 전체 쪽수, A가 찾을, B가 찾을
    P, A, B = map(int, input().split())

    A_num = find_page(A, P)
    B_num = find_page(B, P)

    if A_num > B_num:
        result = 'B'
    elif A_num < B_num:
        result = 'A'
    else:
        result = 0

    print(f'#{t} {result}')
