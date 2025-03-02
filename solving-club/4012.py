import sys
from pathlib import Path

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
    
    if i == N:    # 끝까지 탐색했으면 되돌아가기
        return
    
    if len(arr) == N//2:    # 선택한 개수가 재료 개수의 절반일 때
        others = []    # B에게 만들어줄 요리의 재료들
        for kind in range(N):
            if kind not in arr:
                others.append(kind)

        syn1, syn2 = 0, 0    # A, B에게 만들어줄 요리의 재료들의 시너지 합
        for i in range(N//2-1):
            for j in range(i+1, N//2):
                syn1 += (S[arr[i]][arr[j]]+S[arr[j]][arr[i]])
                syn2 += (S[others[i]][others[j]]+S[others[j]][others[i]])

        min_gap = min(min_gap, abs(syn1-syn2))    # 가장 작은 차이 구하기
        return

    # 전체 재료 개수의 절반 만큼 넣을 때까지 계속
    checked[i] = True    # 사용여부 체크
    arr.append(i)    # A에게 넣어주기
    dfs(i+1, arr)    # 다음 인덱스로 이동
    
    # 백트래킹
    checked[i] = False
    arr.pop()
    dfs(i+1, arr)


# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 종류
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]

    # 선택했는지
    checked = [False] * N

    # 선택된 것들 넣어주는
    picked = []

    # 최소 차이
    min_gap = float('inf')

    dfs(0, picked)

    answer = min_gap

    print(f'#{tc} {answer}')