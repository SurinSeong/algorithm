"""
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""
# DFS
def dfs(v, n):
    # visited, stack 를 함수 밖에서도 사용하고 싶다면 밖에서 만들어두고 써도 된다.
    visited = [0] * (n+1)
    stack = []
    top = -1

    while True:
        # 첫 방문이면
        if visited[v] == 0:
            # 방문했다고 표시만 해주기
            visited[v] = 1
            print(v)

        # v에 인접한 것을 확인
        for w in adj_list[v]:
            # v에 인접하고 방문하지 않은 w가 있으면
            if visited[w] == 0:
                top += 1
                stack[top] = w
                # 현재 위치 변경
                v = w
                break
        # 더이상 갈 곳이 없으면
        else:
            # 스택이 비어있지 않다면
            if stack:
                top -= 1
                v = stack[top]
            # 스택이 비었다면
            else:
                # 다 돈거니간 끝내기
                break


V, E = map(int, input().split())
graph = list(map(int, input().split()))
# 방법 1
# 2차원 배열(VxV)을 이용한 방법 => 인접 행렬
# 방법 2
# adj_list 생성
adj_list = [[] for _ in range(V+1)]
# i행 : i번 정점에 인접한 정점 번호
# 한 번에 2개씩 읽어오기 -> 인덱스 2개씩 건너뛰면서 읽는 방법도 있음.
for i in range(E):
    v, w = graph[i*2], graph[i*2+1]

    adj_list[v].append(w)
    adj_list[w].append(v)

dfs(i, V)