import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_4881.txt'
sys.stdin = open(filename, 'r')

"""
NxN 배열에 숫자가 있음.
한 줄에 하나씩 N개의 숫자를 골라 합이 최고
세로 줄에 하나만 선택
"""
def process_solution(a, k):    # 최솟값 얻는 함수
    global result
    
    # 각 행에서 선택한 열의 숫자의 합을 계산한다.
    total_sum = 0
    
    for i in range(k):    # k까지 선택한 행들에 대해
        total_sum += matrix[i][a[i]]
    
    result = min(result, total_sum)


def construct_candidates(a, k, n, c):    # k번째 행에서 선택할 수 있는 열을 구한다.
    # 이미 사용된 열을 제외하고 후보로 남은 열을 c 배열에 저장한다.
    col_used = [False] * n
    
    for i in range(k):    # 지금까지의 행까지 중에서
        col_used[a[i]] = True    # 이전 행에서 사용한 열은 선택할 수 없다.
        
    ncandidates = 0    # 후보 개수
    for i in range(n):
        if not col_used[i]:    # 아직 선택되지 않은 열만 후보로 추가한다.
            c[ncandidates] = i
            ncandidates += 1
            
    return ncandidates 


def backtrack(a, k, n, s):
    global result
    
    c = [0]*N    # 후보 열 저장하는 리스트
    
    if s >= result:
        return
    
    elif k == n:    # 각 행마다 특정 열을 모두 선택했다면
        process_solution(a, k)    # 모든 행에 대해 숫자를 선택했으면 결과를 처리한다.
    
    else:
        ncandidates = construct_candidates(a, k, n, c)    # 후보 열을 구한다.
        for i in range(ncandidates):    # 후보 번호 돌기
            a[k] = c[i]    # 후보 선택해서
            backtrack(a, k+1, n, s+matrix[k][a[k]])    # 다음 행으로 이동한다.
            # backtrack(a, k+1, n, s)


# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 배열 크기
    N = int(input())
    # 배열
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    result = float('inf')    # 비교하기 위해 가장 큰 수로 일단 저장
    a = [0] * N    # 각 행에서 선택한 열을 저장하는 배열
    
    backtrack(a, 0, N, 0)
    
    print(f'#{tc} {result}')
    
                
                