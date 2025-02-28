import sys
from pathlib import Path
import itertools

filename = Path.cwd() / 'solving-club/input/input_4012.txt'
sys.stdin = open(filename, 'r', encoding='utf-8')

"""
[요리사]
- 두 명의 손님에게 음식 제공
- N개의 식재료
- N/2개씩 나누어 두 개의 요리
- A, B의 차이가 최소
- 음식의 맛은 음식을 구성하는 식재료들의 조합에 따라 다르게
- table의 값들이 시너지값
- A : 시너지값의 합, B : 시너지값의 합 => 맛의 차이 : |A-B|
"""
def dfs(i, arr):
    global min_gap

    if len(arr) == N//2:
        others = []
        for food in kind_of_food:
            if food not in arr:
                others.append(food)

        syn1, syn2 = 0, 0
        for i in range(N//2-1):
            for j in range(i, N//2):
                syn1 += (S[arr[i]][arr[j]]+S[arr[j]][arr[i]])
                syn2 += (S[others[i]][others[j]]+S[others[j]][others[i]])

        min_gap = min(min_gap, abs(syn1-syn2))
        return

    checked[i] = True
    arr.append(kind_of_food[i])
    dfs(i+1, picked)
    checked[i] = False


# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 종류
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]

    # 종류 나누기
    kind_of_food = [n for n in range(N)]

    # 선택했는지
    checked = [False] * N

    # 선택된 것들 넣어주는
    picked = []

    # 최소 차이
    min_gap = float('inf')

    dfs(0, picked)

    answer = min_gap

    print(f'#{tc} {answer}')