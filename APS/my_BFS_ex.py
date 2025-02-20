# BFS 연습문제
"""
다음은 연결되어 있는 두 개의 정점 사이의 간선을 순서대로 나열해 놓은 것이다.
모든 정점을 너비우선탐색하여 경로를 출력하시오.
시작 정점 : 1

7 8
4 2 1 2 1 3 5 2 4 6 5 6 6 7 3 7
"""
# 출발점에서 어떤 정점까지 거리가 가장 짧은 것부터 탐색하는 것이다. ==> 최단 거리를 구할 때 많이 사용한다.
def bfs(s, e):    # 시작 정점, 마지막 정점
    visited = [0] * (e+1)    # 방문 여부 확인 리스트
    q = []    # 큐 생성
    q.append(s)    # 시작점 인큐
    visited[s] = 1    # 시작점 방문 표시

    while q:    # 큐가 비워질 때까지 반복 (= front != rear)
        t = q.pop(0)    # 디큐해서 t에 저장 (만약 pop()을 쓴다면 dfs(내가 갈 수 있는 곳을 미리 저장하는)가 된다.) ** 중요 **
        print(t)    # t 정점에 대한 처리 ==> 만약 미로였다면 출구인지 확인하는 작업이 들어가면 되겠다.
        for w in adj_list[t]:    # t에 인접한 정점(w) 중
            if visited[w] == 0:    # 인큐 되지 않은 정점 찾으면
                q.append(w)    # 인큐 + 방문표시
                visited[w] = visited[t] + 1    # 몇번 그룹에 의해 방문이 되었는지 확인하기 ==> ** 활용성이 높음 **

    print(visited)

# 만약 한명의 친구가 가까운 친구에게 동시 문자를 발송한다고 하고, 문자를 받은 친구는 다시 문자를 받지 않기로 한다.
# 같은 시간에 문자를 받은 사람을 찾을 경우, 위의 visited 요소를 확인하면 되겠다!
# 탐색에서 얻어진 정보를 이용해 활용하는 경우가 많다. ==> visited 값의 활용도가 높음!
# 시작점에서 최소 몇개의 간선을 거쳐야 특정 점으로 가는지?


# 노드 개수, 인접 개수 받기
N, W = map(int, input().split())

# 인접 노드 받기
node_list = list(map(int, input().split()))

# 인접 리스트 생성하기
adj_list = [[] for _ in range(N+1)]

for i in range(W):
    start = node_list[i*2]
    end = node_list[i*2+1]

    adj_list[start].append(end)
    adj_list[end].append(start)    # 방향이 없는 경우

bfs(5, 7)
