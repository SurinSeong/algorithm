import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_4836.txt'
sys.stdin = open(filename, 'r')

# 테스트 케이스 수
T = int(input())

for t in range(1, T+1):
    matrix = [[0]*10 for _ in range(10)]
    # 보라색이 된 칸의 개수
    purple = 0
    # 칠할 영역 개수
    N = int(input())
    
    for _ in range(N):
        # 모서리 인덱스, 색상정보 받기
        r1, c1, r2, c2, color = map(int, input().split())
        
        # 범위 잡아서 색칠하기
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                matrix[r][c] += color
                
                if matrix[r][c] == 3:
                    purple += 1
    
    print(f'#{t} {purple}')
                
                
                
    