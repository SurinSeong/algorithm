# 풍선팡
# NxM
# 본인 + 상하좌우
# 날릴 수 있는 꽃가루의 합 중 최대는?
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_9490.txt'
sys.stdin = open(filename, 'r')


# for를 바꿔보자
def total_flowers(y, x, n, m, matrix):
    # 자기 자신과 주변 꽃가루 합친 것
    total = matrix[y][x]
    # 상하좌우
    delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for dy, dx in delta:
        for k in range(1, matrix[y][x]+1):
            new_y, new_x = y + dy*k, x + dx*k
            if (0 <= new_y < n) and (0 <= new_x < m):
                total += matrix[new_y][new_x]
            else:
                break
    return total


# 테스트 케이스
T = int(input())

for t in range(1, T+1):
    # N, M
    N, M = map(int, input().split())
    # 풍선 배열
    balloons = [list(map(int, input().split())) for _ in range(N)]

    # 가장 많은 꽃가루 개수
    max_total = 0

    for i in range(N):
        for j in range(M):
            current_total = total_flowers(i, j, N, M, balloons)
            max_total = max(max_total, current_total)

    print(f'#{t} {max_total}')
