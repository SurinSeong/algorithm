# 노드의 거리
"""
노드의 개수 : V / 방향성이 없는 간선 : E

주어진 출발 노드로부터 도착 노드까지 최소한의 간선 수는? 경로가 없다면 0
"""
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_5102.txt'
sys.stdin = open(filename, 'r', encoding='utf-8')


def bfs(s, e, n):
    visited = [0] * (n+1)    # 노드 개수 + 1 만큼 방문 확인 리스트 생성
    q = []    # 큐 생성
    q.append(s)    # 출발 노드 인큐
    visited[s] = 1    # 방문 확인

    while q:    # 큐가 비어 있지 않다면 반복
        t = q.pop(0)    # 현재 위치 디큐
        if t == e:    # 만약 현재 위치가 도착이라면
            return visited[t] - 1

        # 아직 도착을 발견하지 못했다면
        for w in adj_list[t]:    # 인접 리스트에서 인접 노드 찾기
            if visited[w] == 0:    # 만약 방문하지 않았다면
                q.append(w)    # 인큐
                visited[w] = visited[t] + 1    # 방문 기록 업데이트

    return 0    # 경로가 없다면


# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 노드의 개수, 간선의 개수
    V, E = map(int, input().split())
    # 인접 리스트
    adj_list = [[] for _ in range(V+1)]

    # 간선의 양쪽 노드 번호 반복
    for _ in range(E):
        s, e = map(int, input().split())

        adj_list[s].append(e)
        adj_list[e].append(s)    # 방향성이 없기 때문에

    # 출발, 도착 노드
    S, G = map(int, input().split())

    answer = bfs(S, G, V)

    print(f'#{tc} {answer}')