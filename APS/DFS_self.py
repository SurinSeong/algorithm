"""
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""
# DFS 만들기
def dfs(s, n, relation):    # s : 시작 노드, n 총 노드 수
    # visited, stack
    stack = [0]*(n+1)
    top = -1
    visited = [0]*(n+1)    # 이미 방문한 곳

    while True:
        if visited[s] == 0:    # 첫 방문
            visited[s] = 1    # 방문 표시
            print(s)

        for other in relation[s]:    # 특정 하나의 노드에 인접한 것 확인하기
            if visited[other] == 0:    # 아직 방문하지 않은 노드라면
                top += 1
                stack[top] = other    # push
                s = other    # 시작노드를 현재의 노드로 업데이트
                break    # 다음 노드를 시작으로 다시 깊게 들어가야 하기 때문에

        else:    # 더 이상 갈 곳이 없다면 (모두 visited가 1이어서 if문이 실행되지 않음)
            if top != 0:    # 스택이 비지 않았다면
                top -= 1
                s = stack[top]    # 이전의 노드로 올라간다.
            else:    # 스택이 비었다면
                # 끝내기
                break


N, V = map(int, input().split())
related = list(map(int, input().split()))

new_related = {}
for i in range(V):
    start, end = related[i*2], related[i*2+1]

    if start not in new_related:
        new_related[start] = [end]
    else:
        new_related[start].append(end)

    if end not in new_related:
        new_related[end] = [start]
    else:
        new_related[end].append(start)

dfs(1, N, new_related)

