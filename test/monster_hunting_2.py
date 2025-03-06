import sys
from pathlib import Path
# from itertools import permutations

filename = Path.cwd() / 'test/input_monster.txt'
sys.stdin = open(filename, 'r')

"""
[헌터]
- 몬스터를 처리하고 요청한 고객에게 확인받으면 작업 완료
- 몬스터 처리 : 몬스터가 있는 위치로
- 헌터가 1시간동안 상하좌우 한 칸씩 갈 수 있음.
- 모든 작업을 가장 빨리 완료할 수 있는 경우는?

[조건]
- N x N (3 <= N <= 10)
- 고객 및 몬스터의 개수 : 1 <= M <= 4
- 몬스터는 양수, 고객은 음수
- 헌터의 첫 위치 : 0,0
"""
# dfs 도전
def dfs(i, monsters, clients, L):

    if i == N:
        return

    ci, cj = total[i][0], total[i][1]
    if map_info[ci][cj] > 0:    # 몬스터라면
        monsters[map_info[ci][cj]] = True
        dfs(i+1, monsters, clients, L+[[ci, cj]])
        monsters[map_info[ci][cj]] = False

    if map_info[ci][cj] < 0:
        if monsters[abs(map_info[ci][cj])]:
            clients


T = int(input())

for tc in range(1, T+1):
    # 맵 길이
    N = int(input())
    # 맵 정보
    map_info = [list(map(int, input().split())) for _ in range(N)]
    # 헌터의 첫 위치
    R, C = 0, 0
    # 몬스터, 고객 방문 관련
    monsters, clients = [0]*5, [0]*5

    # 몬스터, 고객 좌표 구하기
    total = []

    for i in range(N):
        for j in range(N):
            if map_info[i][j] > 0:
                total.append((i, j))

            if map_info[i][j] < 0:
                total.append((i, j))

    min_time = float('inf')




    print(f'#{tc} {min_time}')
