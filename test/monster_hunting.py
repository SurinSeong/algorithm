import sys
from pathlib import Path
from itertools import permutations

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
# 몬스터, 고객의 좌표를 알아낸다.
def find_monster_and_clients():
    for i in range(N):
        for j in range(N):
            if map_info[i][j] > 0:
                monsters[map_info[i][j]-1] = (i, j)     # 좌표 저장하기
                total.append(map_info[i][j])

            if map_info[i][j] < 0:
                clients[map_info[i][j]*(-1)-1] = (i, j)    # 좌표 저장하기
                total.append(map_info[i][j])



# 몬스터 잡기
def hunting_monsters(order):
    global R, C, min_time

    current_time = 0
    hi, hj = R, C    # 헌터 위치
    for num in order:
        if num > 0:
            ci, cj = monsters[num-1][0], monsters[num-1][1]
        elif num < 0:
            ci, cj = clients[num*(-1)-1][0], clients[num*(-1)-1][1]

        # 시간 구하기
        current_time += (abs(hi-ci)+abs(hj-cj))
        # 헌터 위치 업데이트
        hi, hj = ci, cj

    # 가장 짧은 시간 업데이트
    min_time = min(min_time, current_time)


T = int(input())

for tc in range(1, T+1):
    # 맵 길이
    N = int(input())
    # 맵 정보
    map_info = [list(map(int, input().split())) for _ in range(N)]
    # 헌터의 첫 위치
    R, C = 0, 0
    # 몬스터, 고객 방문 관련
    total = []
    monsters, clients = [0]*4, [0]*4

    find_monster_and_clients()    # 몬스터와 고객의 좌표 저장하기

    # 알아낸 몬스터와 고객을 순열돌린다
    sorted_perms = []
    for perm in permutations(total, len(total)):
        if perm[0] < 0:
            continue
        for i in range(1, len(perm)):
            pre = perm[:i]
            if (perm[i] < 0) and (perm[i]*(-1) not in pre):    # 만약 음수인데 이전 리스트에서 -1한 것이 나오지 않았으면
                break
        else:
            sorted_perms.append(perm)

    min_time = float('inf')

    # 몬스터 잡으면서 최소 시간을 구한다.
    for order in sorted_perms:
        hunting_monsters(order)

    print(f'#{tc} {min_time}')
