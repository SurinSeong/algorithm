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
def cal_square_sum(num_list):
    return sum(num**2 for num in num_list)


# 테스트 케이스 개수
T = int(input())

for x in range(1, T+1):
    # 벌통 크기, 벌통 수, 최대
    N, M, C = map(int, input().split())

    # 벌통 정보
    honey = [list(map(int, input().split())) for _ in range(N)]
    # 새로운 배열 만들기
    matrix = [[0]*(N-M+1) for _ in range(N)]

    # 첫번째 일꾼이 m개 선택
    for i1 in range(N):
        for j1 in range(N-M+1):
            # 첫 번째가 선택한 벌꿀 리스트
            first_select_honey_list = honey[i1][j1:j1+M]
            first_select_honey_max = 0

            # 부분 집합은 => 1부터 N개까지 각각 선택하는 조합의 모든 경우의 수
            for select_cnt in range(1, M+1):
                comb = itertools.combinations(first_select_honey_list, select_cnt)
                # 조합에서 이익 구하기
                first_comb_list = list(map(cal_square_sum, comb))
                # 제곱의 합의 최댓값 업데이트
                first_select_honey_max = max(max(first_comb_list), first_select_honey_max)

            for i2 in range(i1, N):
                for j2 in range(0, N-M+1):
                    if i1 == i2 and i2 < i1+M:
                        continue
                    # 첫 번째가 선택한 벌꿀 리스트
                    first_select_honey_list = honey[i1][j1:j1 + M]
                    first_select_honey_max = 0

                    # 부분 집합은 => 1부터 N개까지 각각 선택하는 조합의 모든 경우의 수
                    for select_cnt in range(1, M + 1):
                        comb = itertools.combinations(first_select_honey_list, select_cnt)
                        # 조합에서 이익 구하기
                        first_comb_list = list(map(cal_square_sum, comb))
                        # 제곱의 합의 최댓값 업데이트
                        first_select_honey_max = max(max(first_comb_list), first_select_honey_max)


    calculate_double(honey, N, M, C)

    answer = find_max_total(matrix, N, M, C)

    print(f'#{x} {answer}')