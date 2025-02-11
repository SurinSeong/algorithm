# 파리퇴치 3
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_12712.txt'
sys.stdin = open(filename, 'r')

# NxN
# +, x
# M의 세기 (벗어나도 상관없음)

def total_files(row, col, K, N):
    
    global flies
    
    # 상하좌우 델타
    delta1 = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    # 대각선 델타
    delta2 = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
    # 더 큰 값을 넣기 위해
    max_total = 0
    
    for delta in [delta1, delta2]:
        
        # 총합
        total = flies[row][col]
        
        for di, dj in delta:
            for k in range(1, K):
                new_i, new_j = row + di*k, col + dj*k
                # 범위 안에 있으면
                if (0 <= new_i < N) and (0 <= new_j < N):
                    total += flies[new_i][new_j]
        
        max_total = max(max_total, total)
        
    return max_total


# 테스트 케이스 개수
T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    # 파리 매트릭스
    flies = [list(map(int, input().split())) for _ in range(N)]
    # 가장 큰 값은?
    max_flies = 0
    
    for i in range(N):
        for j in range(N):
            current_flies = total_files(i, j, M, N)
            max_flies = max(max_flies, current_flies)
        
    print(f'#{t} {max_flies}')