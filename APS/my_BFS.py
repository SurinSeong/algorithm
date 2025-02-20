# BFS 알고리즘
"""
입력 파라미터 : 그래프 G와 탐색 시작점 v
"""
# 기본
def BFS(G, v):    # 그래프 G, 탐색 시작점 v
    visited = [0] * (n+1)    # 방문 여부 확인 리스트, n : 노드 개수
    q = []    # 큐 생성
    q.append(v)    # 시작점 v를 큐에 삽입
    visited[v] = 1
    while q:   # 큐가 비어있지 않은 경우
        t = q.pop(0)    # 큐의 첫 번째 원소 반환
        visit(t)    # 정점 t에서 할일
        for i in G[t]:    # t와 연결된 모든 정점에 대해
            if not visited[i]:    # 방문되지 않은 곳이라면
                q.append(i)    # 큐에 넣기
                visited[i] = visited[t] + 1    # t으로부터 인접한 것들을 하나씩 더한 값이 기록되도록 한다.

