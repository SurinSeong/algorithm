# 두개의 숫자열
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_1959.txt'
sys.stdin = open(filename, 'r')

# 테스트 케이스
T = int(input())

for t in range(1, T+1):
    # A의 길이, B의 길이
    N, M = map(int, input().split())
    # A
    A = list(map(int, input().split()))
    # B
    B = list(map(int, input().split()))

    # 길이가 더 긴 것 찾기
    if N > M:
        long_list, short_list = A, B
    else:
        short_list, long_list = A, B

    # 곱이 가장 큰 합
    max_sum = float('-inf')

    for i in range(abs(N-M)+1):
        multi = 0
        for k in range(len(short_list)):
            multi += (long_list[k+i]*short_list[k])

        max_sum = max(max_sum, multi)

    print(f'#{t} {max_sum}')