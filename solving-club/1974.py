# 스도쿠 검증
# 9 x 9
# 잘 되었으면 1, 아니면 0
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_1974.txt'
sys.stdin = open(filename, 'r')

# 테스트 케이스 개수
T = int(input())

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for t in range(1, T+1):
    # 스도쿠 입력받기
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    
    # 가로, 세로, 대각선으로 가면서 확인해보기
    for i in range(9):
        # 행, 열별 숫자들
        row_numbers, col_numbers = [], []
        for j in range(9):
            row_numbers.append(sudoku[i][j])
            col_numbers.append(sudoku[j][i])
        
            # 3x3에서        
            if ((i+2) % 3 == 0) and ((j+2) % 3  == 0):
                box_numbers = []
                delta = [[0, 0], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
                for di, dj in delta:
                    box_numbers.append(sudoku[i + di][j + dj])
                    
                if len(set(box_numbers)) != 9:
                    result = 0
                    break
                
            # 1~9까지 모두 있는지 확인
        if (set(row_numbers) != set(numbers)) or (set(col_numbers) != set(numbers)):
            result = 0
            break
    else:
        result = 1
                       
    print(f'#{t} {result}')