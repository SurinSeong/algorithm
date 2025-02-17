import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_11092.txt'
sys.stdin = open(filename, 'r')

"""
[최대값과 최소값]
- N개의 양의 정수
- 첫 번째 ~ N 번째
- 결과 : |최댓값의 위치 - 최솟값의 위치|
- 가장 작은 수가 여러 개이면, 먼저 나오는 위치
- 가장 큰 수가 여러 개이면 마지막으로 나오는 위치
"""


def min_max_index_gap(arr, n):
    min_idx, max_idx = 0, 0
    for i in range(1, n):
        if arr[max_idx] <= arr[i]:
            max_idx = i

        if arr[min_idx] > arr[i]:
            min_idx = i

    return max_idx - min_idx


# 테스트 케이스 개수
T = int(input())

for test_case in range(1, T+1):
    # 양수의 개수
    N = int(input())
    # 양수 리스트
    a = list(map(int, input().split()))

    result = min_max_index_gap(a, N)

    if result < 0:
        result *= -1

    print(f'#{test_case} {result}')