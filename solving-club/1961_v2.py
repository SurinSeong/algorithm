# 숫자 배열 회전
# NxN 행렬 -> 90, 180, 270
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_1961.txt'
sys.stdin = open(filename, 'r')

# 테스트 케이스 개수
T = int(input())

for t in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    print(f'#{t}')
    
    for i in range(N):
        rotation_90 = ''
        rotation_180 = ''
        rotation_270 = ''
        # 규칙으로 돌면서 str로 더하기
        for j in range(N):
            rotation_90 += str(matrix[N-1-j][i])
            rotation_180 += str(matrix[N-1-i][N-1-j])
            rotation_270 += str(matrix[j][N-1-i])
            
        print(f'{rotation_90} {rotation_180} {rotation_270}')
    
    