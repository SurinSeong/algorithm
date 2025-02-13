import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_2005.txt'
sys.stdin = open(filename, 'r')

# 파스칼의 삼각형
# 크기가 N인 삼각형 출력
# 재귀..?


def pascal(i, n, arr):
    if n == i:
        return
    else:
        for j in range(i+1):
            if i == 0:
                print(arr[i][j], end='')
                break
            if j == 0:
                arr[i][j] += arr[i-1][j]
            else:
                arr[i][j] += (arr[i-1][j-1] + arr[i-1][j])
            print(arr[i][j], end=' ')
        print()
        return pascal(i+1, n, arr)


# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 삼각형의 크기
    N = int(input())
    # NxN 배열 만들기
    matrix = [[0]*N for _ in range(N)]
    matrix[0][0] = 1

    print(f'#{tc}')
    result = pascal(0, N, matrix)


