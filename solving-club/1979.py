# 어디에 단어가 들어갈 수 있을까
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_1979.txt'
sys.stdin = open(filename, 'r')

# 테스트 케이스
T = int(input())

for t in range(1, T+1):
    # 가로 세로, 단어길이
    N, K = map(int, input().split())
    # 퍼즐
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    # 단어가 들어갈 수 있는 곳의의 개수
    total = 0
    for i in range(N):
        for j in range(N):
            # 흰 부분이라면
            if puzzle[i][j] == 1:
                # 우하
                delta = [[0, 1], [1, 0]]
                for di, dj in delta:
                    # 단어길이+1에서 부터 확인
                    for k in range(1, K+1):
                        next_i, next_j = i + di*k, j + dj*k
                        # N x N 안에 있는 범위 인가 확인하기
                        if (0 <= next_i < N) and (0 <= next_j < N):
                            # 검은색인지 확인하기
                            if puzzle[next_i][next_j] == 0:
                                break
                        # 범위 안에 없다면
                        else:
                            break
                    else:
                        # 다음 위치가 검은색인지 확인하기
                        next_i, next_j = i + di*(K+1), j + dj*(K+1)
                        # 
                        if (0 <= next_i < N) and (0 <= next_j < N) and (puzzle[next_i][next_j] == 0):
                            total += 1
    
    print(f'#{t} {total}')