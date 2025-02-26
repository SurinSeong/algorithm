import sys
from pathlib import Path
import itertools
#
filename = Path.cwd() / 'solving-club/input/input_2115.txt'
sys.stdin = open(filename, 'r', encoding='utf-8')

"""
[벌꿀채취]
- NxN -> 3~10
- 최대한 많은 수익
- 두 명의 일꾼. 꿀을 채취할 수 있는 벌통의 수 M -> 1~5
- 가로로 연속되도록 M개의 벌통 선택
- 두 일꾼의 벌통은 겹치면 안됨
- 두 일꾼이 채취할 수 있는 꿀의 최대 양은 C
- 수익의 합이 최대
"""
def calculate_double(arr, n, m, c):
    for i in range(n):
        for j in range(n-m+1):
            can_get = arr[i][j:j+m]

            total = 0

            cnt = 1
            while cnt <= m:
                candidates = list(itertools.combinations(can_get, cnt))

                for candidate in candidates:
                    if len(candidate) == 1:
                        if candidate[0] <= c:
                            current_total = candidate[0]**2
                    else:
                        if sum(candidate) <= c:
                            current_total = 0
                            for num in candidate:
                                current_total += num**2
                    total = max(total, current_total)
                cnt += 1

            matrix[i][j] = total


def find_max_total(arr, n, m, c):
    max_total = 0
    # 첫번째 일꾼 찾기
    for i in range(n):
        for j in range(n-m+1):
            first = arr[i][j]

            for i2 in range(n):
                if i2 == i:
                    if j+c < n-m+1:
                        for j2 in range(j+c, n-m+1):
                            second = arr[i2][j2]
                            max_total = max(first+second, max_total)
                else:
                    for j2 in range(n-m+1):
                        second = arr[i2][j2]
                        max_total = max(first+second, max_total)
    return max_total


# 테스트 케이스 개수
T = int(input())

for x in range(1, T+1):
    # 벌통 크기, 벌통 수, 최대
    N, M, C = map(int, input().split())

    # 벌통 정보
    honey = [list(map(int, input().split())) for _ in range(N)]
    # 새로운 배열 만들기
    matrix = [[0]*(N-M+1) for _ in range(N)]

    calculate_double(honey, N, M, C)

    answer = find_max_total(matrix, N, M, C)

    print(f'#{x} {answer}')