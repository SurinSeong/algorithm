# import sys
# from pathlib import Path

# filename = Path.cwd() / 'solving-club/input/input_2105.txt'
# sys.stdin = open(filename, 'r', encoding='utf-8')

"""
[디저트 카페]
- N x N
- 대각선으로 움직인다
- 같은 숫자의 디저트를 팔고 있는 카페가 있으면 안됨.
- 왔던 길 돌아오기도 안됨.
- 출발한 곳으로 돌아와야 함.
- 가장 많이 먹을 수 있는 경로 -> 디저트 수?
"""
def find_max_dessert(i, j, d, cnt, dessert, si, sj):
    global max_desserts, max_cnt
    
    visited[i][j] = True
    kind_of_dessert.append(cafes[i][j])
    
    di, dj = delta[d][0], delta[d][1]
    
    if 0 <= i+di < N and 0 <= j+dj < N:
        if not visited[i+di][j+dj] and (cafes[i+di][j+dj] not in kind_of_dessert):    # 방문한 적도 없고 새로운 디저트 종류라면
            find_max_dessert(i+di, j+dj, d, cnt+1, dessert+cafes[i+di][j+dj], i, j)
        
        if cafes[i+di][j+dj] in kind_of_dessert:
            if d < 4:
                find_max_dessert(i, j, d+1, cnt, dessert, i, j)
        
    # elif d < 4:    # 배열 안에 없는데 delta 인덱스가 4를 넘지 않았다면
    #     find_max_dessert(i, j, d+1, cnt, dessert, i, j)
        
    if si == i and sj == j:    # 시작점으로 돌아왔다면
        if max_desserts < dessert:    # 현재까지의 총 디저트 개수보다 max가 작다면
            max_cnt = cnt    # 현재의 디저트 종류 개수로 바꿔준다.
            visited[i][j] = False
    


# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cafes = [list(map(int, input().split())) for _ in range(N)]
    
    # 대각선으로 갈 델타
    delta = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
    
    max_desserts, max_cnt = 0, 0
    
    visited = [[False]*N for _ in range(N)]
    kind_of_dessert = []
    
    # 시작점 잡아주기
    for i in range(N-1):
        for j in range(1, N):
            find_max_dessert(i, j, 0, 1, cafes[i][j], i, j)
    
    if max_cnt == 0:
        answer = -1
    else:        
        answer = max_cnt
    
    print(f'#{tc} {answer}')

