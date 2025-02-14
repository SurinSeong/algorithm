# 숫자 배열 회전
# NxN 행렬 -> 90, 180, 270
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_1961.txt'
sys.stdin = open(filename, 'r')


# 더 쉽게 할 수 있는 것이 있을 듯..
def rotation_list(data, n):
    rotation_90 = list(map(list, zip(*data[::-1])))
    rotation_180 = list(map(list, zip(*rotation_90[::-1])))
    rotation_270 = list(map(list, zip(*rotation_180[::-1])))

    rotations = [rotation_90, rotation_180, rotation_270]

    new_matrix = [[''] * 3 for _ in range(n)]

    for i in range(n):
        for k in range(3):
            for j in range(n):
                new_matrix[i][k] += str(rotations[k][i][j])

    return new_matrix


# 테스트 케이스
T = int(input())

for t in range(1, T+1):
    # NxN
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # 모두 회전한 것 생성
    matrix_list = rotation_list(matrix, N)

    print(f'#{t}')

    for row in range(N):
        for col in range(3):
            print(matrix_list[row][col], end=' ')
        print()
