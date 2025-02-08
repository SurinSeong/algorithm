import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_1209.txt'
sys.stdin = open(filename, 'r')

for _ in range(1, 11):
    # 테스트 케이스 번호
    t = int(input())
    # 100x100 배열 받기
    matrix = [list(map(int, input().split())) for _ in range(100)]
    
    # 대각선 합
    left_cross, right_cross = 0, 0
    # 대각선 중 가장 큰수, 가로 세로 중 가장 큰 수
    cross_max, line_max = 0, 0
    
    for i in range(100):
        # 가로 세로 합
        row_sum, col_sum = 0, 0
        for j in range(100):
            # 행과 열의 인덱스가 같다면
            if i == j:
                left_cross += matrix[i][j]

            elif i == (100 - 1 - j):
                right_cross += matrix[i][j]
            
            # 가로 세로
            row_sum += matrix[i][j]
            col_sum += matrix[j][i]  
            
        if line_max < row_sum:
            line_max = row_sum
        if line_max < col_sum:
            line_max = col_sum
            
    if left_cross < right_cross:
        cross_max = right_cross
    else:
        cross_max = left_cross
    
    print(f'#{t} {max(cross_max, line_max)}')
              
            

