# 어디에 단어가 들어갈 수 있을까?
# NxN
# 특정 길이 K
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_1979.txt'
sys.stdin = open(filename, 'r')

# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 가로세로, 단어길이
    N, K = map(int, input().split())
    # 퍼즐
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    # 들어갈 칸 수
    total = 0
    for i in range(N):
        possible_row = 0
        possible_col = 0
        for j in range(N):
            # 행 확인
            # 흰색이면 추가
            if puzzle[i][j]:
                possible_row += 1
            # 검은색이면 이제까지의 possible 확인하기
            else:
                if possible_row == K:
                    total += 1
                possible_row = 0
            # 열 확인
            if puzzle[j][i]:
                possible_col += 1
            else:
                if possible_col == K:
                    total += 1
                possible_col = 0
        
        if possible_row == K:
            total += 1
        if possible_col == K:
            total += 1
    
    print(f'#{tc} {total}')            