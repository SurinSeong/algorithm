# 그래프 경로
# # V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프에 대한 정보가 주어질 때
# # 특정한 두 개의 노드에 경로가 존재하는지 확인하는 프로그램 1, 0
import sys
from pathlib import Path

filename = Path.cwd() / 'solving-club/input/input_21648.txt'
sys.stdin = open(filename, 'r', encoding='utf-8')

# 갈 수 있는지 확인하기
def is_possible(s, e):
    # 확인했는지에 대한 리스트
    visited = [0]*(V+1)
    # stack
    stack = [0]*V
    top = -1
    # start 값을 넣어주고 시작한다.
    visited[s] = 1
    top += 1
    stack[top] = s

    while True:
        # 인접 정점 탐색
        for w in adj_list[s]:
            # 인접 정점이 원하는 끝이라면
            if w == e:
                # 갈 수 있음.
                return 1

            # 방문하지 않았다면
            if not visited[w]:
                # 상태 변경
                visited[w] = 1
                # 시작 위치 옮겨주기
                top += 1
                stack[top] = w
                s = w
                break
        # 다돌았는데 못찾았으면
        else:
            # 하나 뺄 준비하기
            top -= 1
            # 만약 top != -1 이라면
            if top != -1:
                s = stack[top]
                continue
            # 비었다면..
            return 0



# 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 노드, 쌍
    V, E = map(int, input().split())
    # 인접 리스트 만들기
    adj_list = [[] for _ in range(V + 1)]
    # 인접 받기
    for _ in range(E):
        v, w = map(int, input().split())
        adj_list[v].append(w)
    # 시작 끝 받기
    start, end = map(int, input().split())

    answer = is_possible(start, end)

    print(f'#{tc} {answer}')

