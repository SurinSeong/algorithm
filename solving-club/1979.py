# 어디에 단어가 들어갈 수 있을까
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_1979.txt'
sys.stdin = open(filename, 'r')

# 테스트 케이스
T = int(input())

for t in range(1, T+1):
    # 가로 세로, 단어 길이
    N, K = map(int, input().split())
    # 퍼즐
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    
    # 단어가 들어갈 수 있는 빈칸의 개수
    total = 0
    # 퍼즐 돌기
    for i in range(N):
        # 줄별 합 확인하기
        row_sum, col_sum = 0, 0
        for j in range(N):
            # 행별 들어갈 수 있는 칸 수 확인하기
            # 검은 색이면 넘기기
            if puzzle[i][j] == 0:
                # 만약 이미 칸수가 다 찼다면
                if row_sum == K:
                    # 단어가 들어갈 수 있음
                    total += 1
                # 칸수 리셋
                row_sum = 0
            # 흰색이면
            else:
                # 칸수에 1씩 더하기
                row_sum += 1
                
            # 열별 들어갈 수 있는 칸 수 확인하기
            # 검은 색이면
            if puzzle[j][i] == 0:
                if col_sum == K:
                    total += 1
                col_sum = 0
            else:
                col_sum += 1
        
        # 각 행을 모두 돌고나서의 칸수 합이 단어의 길이와 같다면
        if row_sum == K:
            # 전체 들어갈 수 있는 칸수에 +1
            total += 1
        
        # 각 열을 돌고 나서 ~
        if col_sum == K:
            total += 1
            
    print(f'#{t} {total}')