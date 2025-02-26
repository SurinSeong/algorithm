# import sys
# from pathlib import Path
from collections import deque

# filename = Path.cwd() / 'solving-club/input/input_4408.txt'
# sys.stdin = open(filename, 'r')

"""
최단 시간에 모든 학생이 자신의 방으로 돌아간다.
방 : 400개
복도가 겹치면 같이 못들어감.
"""
def dfs(arr, n):
    # 방문했던
    visited = [0] * n
    # 스택
    stack = []
    top = -1
    
    
                
                    
# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 돌아가야 할 학생들의 수
    N = int(input())
    # 들어가야 할 학생 리스트
    student_list = []
    # 학생 수 만큼 반복
    for _ in range(N):
        here, move = map(int, input().split())
        student_list.append([min(here, move), max(here, move)])    # 어차피 겹치는 거는 똑같으니깐..
        
    # student_list 정렬시키기
    for i in range(N-1):
        for j in range(i, N):
            if student_list[i][0] > student_list[j][0]:
                student_list[i], student_list[j] = student_list[j], student_list[i]
                
    print(student_list)

    answer = go_back(student_list, N)

    print(f'#{tc} {answer}')