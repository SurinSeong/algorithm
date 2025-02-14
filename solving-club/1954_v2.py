# 달팽이 숫자 >> 다시..
# 1~N*N 숫자가 시계방향으로 작성
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_1954.txt'
sys.stdin = open(filename, 'r')

# 재귀 말고 다른 걸로



# 테스트 케이스 개수
T = int(input())

for t in range(1, T+1):
    # N
    N = int(input())
    # 빈 매트릭스 만들기
    matrix = [[0]*N for _ in range(N)]
    # 우선 가장 첫 번째에 1을 넣어준다.
    matrix[0][0] = 1
    

    print(f'#{t}')
    for i in range(N):
        for j in range(N):
            print(matrix[i][j], end=' ')
        print()