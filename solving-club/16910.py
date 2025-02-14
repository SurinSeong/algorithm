# 원 안의 점
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_16910.txt'
sys.stdin = open(filename, 'r')

import math

# 테스트 케이스 수
T = int(input())

for t in range(1, T+1):
    # N : 원의 반지름
    N = int(input())
    # 전체 정수 좌표 개수
    total = 0
    for i in range(1, N+1):
        total += int(math.sqrt(N**2 - i**2))

    total *= 4
    # x, y축
    total += (4*N + 1)

    print(f'#{t} {total}')
