# 풍선팡 보너스 게임
# 보너스 스테이지 규칙
# NxN
# 어떤 풍선을 터트리면 같은 행과 열의 풍선이 모두 터진다.
# 두 번 터뜨릴 수 있고, 두 번 터트려서 나온 값의 차이가 점수!
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_18575.txt'
sys.stdin = open(filename, 'r')


# 한 점에서 가로세로의 모든 수의 합 구하기
def add_row_and_col(r, c, n):
    total = 0
    
    for dr, dc in delta:
        for k in range(1, n):
            next_r, next_c = r+dr*k, c+dc*k
            # 범위 확인 있는지 없는지
            if (0 <= next_r < n) and (0 <= next_c < n):
                total += matrix[next_r][next_c]
    
    total += matrix[r][c]
       
    return total


# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 격자 크기
    N = int(input())
    # 격자 만들기
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    
    max_result = float('-inf')
    min_result = float('inf')
    
    for i in range(N):
        for j in range(N):
            line_sum = add_row_and_col(i, j, N)
            
            max_result = max(line_sum, max_result)
            min_result = min(line_sum, min_result)
    
    result = max_result - min_result
    
    print(f'#{tc} {result}')