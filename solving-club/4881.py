import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_4881.txt'
sys.stdin = open(filename, 'r')

"""
NxN 배열에 숫자가 있음.
한 줄에 하나씩 N개의 숫자를 골라 합이 최고
세로 줄에 하나만 선택
"""
def dfs(i, j, n):
    visited = [[0]*n for _ in range(n)]    # 방문했는지 여부를 알려주는 리스트 생성
    
    stack = []    # 스택 생성
    
    stack.append([i, j])    # 스택에 삽입
    
    result = 0
    
    while stack:
        ti, tj = stack.pop()
        
        if visited[ti][tj] == 0:
            visited[ti][tj] = 1
            result += matrix[ti][tj]
        
        for wi, wj in adj_list[[ti, tj]]
                
            
        
        
        for d in range(n):
            wi, wj = ti + d, tj + d
            if (0 <= wi < n)



# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 배열 크기
    N = int(input())
    # 배열
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    # 인접한 칸 만들기
    adj_dict = 
    
    for i in range(N):
        idx_list = [idx for idx in range(N)]    # 사용할 컬럼 인덱스
        
        j = 0
        while True:
            
            if idx_list[j] in used:
                
                