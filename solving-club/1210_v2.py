import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_1210.txt'
sys.stdin = open(filename, 'r')


def find_start(i, j, matrix):
    while 0 <= i < 100:
        # 왼쪽이나 오른쪽에 1이 있으면 올라가기
        # 1. 왼쪽
        if (0 <= i < 100) and (0 <= j-1 < 100) and matrix[i][j-1] == 1:
            # 왼쪽으로 몇칸까지 갈 수 있는지 확인하기
            while (0 <= j < 100) and matrix[i][j] == 1:
                j -= 1
            find_start(i-1, j, matrix)
        # 2. 오른쪽
        elif (0 <= i < 100) and (0 <= j+1 < 100) and matrix[i][j+1] == 1:
            while (0 <= j < 100) and matrix[i][j] == 1:
                j += 1
            find_start(i-1, j, matrix)
            
        # 3. 윗부분에 1이 있으면 올라가기
        else:
            find_start(i-1, j, matrix)
        
    return j

# 테스트 케이스
for _ in range(10):
    # 테스트케이스 번호
    t = int(input())
    # 100x100 matrix 받기
    puzzle = [list(map(int, input().split())) for _ in range(100)]

    for x in range(100):
        # 만약 첫 번째가 0이면 길이 없음.
        if puzzle[99][x] == 2:
            break
    # 위에서 찾는 x 부터 시작해서 올라가기
    result = find_start(99, x, puzzle)
    
    print(f'#{t} {result}')