import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_4875.txt'
sys.stdin = open(filename, 'r')


"""
맨 윗줄 : 3 출발
마지막 줄 : 2 도착
통로 : 0
도착 가능하면 1, 아니면 0
"""

def escape_maze(arr, s, e, t):
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    # 네 방향을 돌면서 진행한다.
    for i in range(4):
        new_r, new_c = s[0]+dx[i], s[1]+dy[i]
        
        if arr[new_r][new_c] == e:    # 만약 끝점을 만났다면
            return True
        
        if (arr[new_r][new_c] == 0) and (stack[t] != [new_r][new_c]):    # 만약 이전 경로가 아닌 통로라면
            t += 1
            stack[t] = [new_r, new_c]    # push
            
        s = arr[new_r][new_c]    # 시작점 바꿔주기
        return escape_maze(arr, s, e, t)
    
    # 이전통로와 막힌 곳 뿐만 이라면
    else:
        t -= 1    # pop
        s = stack[t]    # 시작 위치 바꿔주기
        return escape_maze(arr, s, e, t)
    
    if
        
        
        
    
        
    
    
    pass


# 테스트 케이스 개수
T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    
    # 스택 생성
    stack = [0] * (N**2)
    top = -1
    
    print(f'#{test_case}')
    