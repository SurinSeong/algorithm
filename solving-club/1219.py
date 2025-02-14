# 길찾기
# A0 -> B99
# 최대 2개의 갈림길
# 되돌아오는 것 불가능
# 길이 주어질 때 A -> B 가는 길이 존재하는지 알아내는 프로그램 1, 0
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_1219.txt'
sys.stdin = open(filename, 'r', encoding='utf-8')


def dfs(s, e):
    # 방문여부
    visited = [0]*99
    # 스택
    stack = [0]*99
    top = -1
    # 시작점은 일단 방문했고, 스택에 넣어준다.
    visited[s] = 1
    top += 1
    stack[top] = s
    # 경로 찾기 시작
    while True:
        # 현재 위치에서의 인접한 노드 찾기
        for w in adj_list[s]:
            # 인접 노드가 마지막 위치라면
            if w == e:
                return 1
            # 방문하지 않았다면
            if not visited[w]:
                # 상태 변경
                visited[w] = 1
                # 스택에 넣어주기
                top += 1
                stack[top] = w
                s = w
                break
        # 찾지 못했으면 전의 노드로 돌아간다.
        else:
            # 일단 stack 에서 제거해야 하니깐 top 감소
            top -= 1
            # 아직 비어있지 않다면
            if top != -1:
                s = stack[top]
                continue
            # 비었다면
            return 0


for _ in range(10):
    # 테스트케이스 번호, 길의 총 개수
    tc, E = map(int, input().split())

    # 순서쌍
    pairs = list(map(int, input().split()))

    # 인접 리스트
    adj_list = [[] for _ in range(100)]

    for i in range(E):
        v = pairs[i*2]
        w = pairs[i*2+1]
        adj_list[v].append(w)

    A, B = 0, 99

    result = dfs(A, B)

    print(f'#{tc} {result}')
