# Contact
"""
비상 연락망과 연락을 시작하는 당번
가장 나중에 연락을 받게 되는 사람 중 번호가 가장 큰 사람은? ==> visited 활용
이미 연락을 받은 사람에게는 연락하지 않음.
연락 최대 인원 : 100명 ==> 1 ~ 100
없는 번호 존재 가능
노드의 개수 : V / 방향성이 있는 간선 : E

주어진 출발 노드로부터 도착 노드까지 최소한의 간선 수는? 경로가 없다면 0
"""
import sys
from pathlib import Path
from collections import deque

filename = Path.cwd() / 'solving-club/input/input_1238.txt'
sys.stdin = open(filename, 'r', encoding='utf-8')


def bfs(s):
    visited = [0] * 101    # 연락 가능한 최대 인원 + 1
    q = deque()    # 큐 생성
    q.append(s)    # 시작 노드 인큐
    visited[s] = 1    # 방문 기록 업데이트

    while q:    # 큐가 비지 않으면
        t = q.popleft()    # 현재 위치 디큐

        for w in contact_list[t]:    # 현재 위치에서의 인접 리스트 확인
            if visited[w] == 0:    # 아직 방문을 못했다면
                q.append(w)    # 인큐
                visited[w] = visited[t] + 1    # 방문 기록 업데이트

    return visited


# 테스트 케이스 개수
T = 10

for tc in range(1, T+1):
    # 인원수, 시작점
    N, S = map(int, input().split())
    # 인접 리스트
    contact_list = [[] for _ in range(101)]

    with_nodes = list(map(int, input().split()))    # 인접 쌍을 리스트로 받음

    for i in range(N//2):    # 인접 리스트 만들기
        from_n, to_n = with_nodes[i*2], with_nodes[i*2+1]    # 연락을 주는 쌍

        if to_n not in contact_list[from_n]:
            contact_list[from_n].append(to_n)    # 이미 연락망에 들어가 있지 않으면

    result = bfs(S)
    # print(result)

    max_n = 0

    for i in range(1, 101):
        if result[max_n] <= result[i]:
            max_n = i

    print(f'#{tc} {max_n}')
