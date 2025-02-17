import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_9386.txt'
sys.stdin = open(filename, 'r')

"""
N개의 0과 1로 이루어진 수열
연속한 1의 개수 중 최대는?
"""


def find_ones_length(arr, n):
    max_length, current_length = 0, 0
    for i in range(n):
        if arr[i] == 0:
            max_length = max(max_length, current_length)
            current_length = 0
        else:
            current_length += 1

    max_length = max(max_length, current_length)

    return max_length


# 테스트 케이스 개수
T = int(input())

for test_case in range(1, T+1):
    # 수열의 길이
    N = int(input())
    # 수열
    a = list(map(int, input()))

    result = find_ones_length(a, N)

    print(f'#{test_case} {result}')