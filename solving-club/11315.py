# 오목 판정
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_11315.txt'
sys.stdin = open(filename, 'r', encoding='utf-8')


def is_rock_nearby(i, j, n):
    location = []
    delta = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
    for di, dj in delta:
        # 범위 안에 있고
        if (0 <= i+di < n) and (0 <= j+dj < n):
            if omok[i+di][j+dj] == 'o':
                location.append([di, dj])
    return location

# NxN
# 돌이 있거나 없을 수 있음.
# 가로, 세로, 대각선 중 하나의 방향으로 다섯 개 이상 연속한 부분이 있는지 없는지
# 테스트 케이스 수
T = int(input())

for tc in range(1, T+1):
    # 크기
    N = int(input())
    # 판의 구성
    omok = [list(input()) for _ in range(N)]
    # 결과 
    result = 'NO'
    # 순환
    for i in range(N):
        for j in range(N):
            if omok[i][j] == 'o':
                where = is_rock_nearby(i, j, N)
                for di, dj in where:
                    cnt = 1
                    for k in range(1, 5):
                        next_i, next_j = i+di*k, j+dj*k
                        # 범위 안에 있으면
                        if (0 <= next_i < N) and (0 <= next_j < N):
                            if omok[next_i][next_j] == 'o':
                                cnt += 1
                            elif cnt < 5:
                                cnt = 1
                                break
                    else:
                        if cnt >= 5:
                            result = 'YES'
                            break
    
    print(f'#{tc} {result}')