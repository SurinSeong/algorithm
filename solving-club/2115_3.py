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
# 부분 집합 구하기
def dfs(honey_idx, honey_benefit, honey_sum):    # 선택할 벌통의 인덱스, 여태까지 선택한 벌통의 이익, 벌통의 합
    # 누적해서 가져가고 싶은 것이 있을 때
    global part_sum

    # 가지치기
    if honey_sum > C:
        return

    # 선택할 벌통이 M에 도달하면, 최댓값 갱신
    if honey_idx == M:
        part_sum = max(part_sum, honey_benefit)

    cnt_sum = honey[i1][j1+honey_idx]
    cnt_benefit = honey_benefit[i1][j1+honey_idx]**2

    # 현재 꿀을 선택했다면
    dfs(honey_idx+1, honey_benefit+cnt_benefit, honey_sum+cnt_sum)

    # 현재 꿀 선택하지 않았다면
    dfs(honey_idx+1, honey_benefit, honey_idx)


# 테스트 케이스 개수
T = int(input())

for x in range(1, T+1):
    # 벌통 크기, 벌통 수, 최대
    N, M, C = map(int, input().split())

    # 벌통 정보
    honey = [list(map(int, input().split())) for _ in range(N)]
    # 새로운 배열 만들기
    matrix = [[0]*(N-M+1) for _ in range(N)]

    answer = 0

    for i1 in range(N):
        for j1 in range(N-M+1):
            part_sum = 0
            # 부분집합의 최대 이익을 구해라.
            # 선택을 하냐 안하냐
            # 1. 재귀 중단 파라미터 설정 => 선택할 벌통의 인덱스 (M 도달하면 재귀호출 중단)
            # 2. 누적해서 가져가고 싶은 값


    print(f'#{x} {answer}')