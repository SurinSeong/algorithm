# 그래프 탐색 알고리즘

# 너비 우선 탐색
# 입력 : 그래프, 탐색 시작점
# 출력 : 시작점에서 출발해 연결된 꼭짓점


def search_graph(graph, start):
    # 큐 설정
    queue = []
    
    # done 설정
    done = set()
    
    # 시작점 넣어주기
    queue.append(start)
    done.add(start)
    
    # 큐 안에 요소가 존재하는 동안 반복
    while queue:
        # 큐에서 요소 빼내기
        target = queue.pop(0)
        print(target)
        # target과 연결된 요소를 돌기
        for vertex in graph[target]:
            # 완료된 집합에 존재하지 않는다면
            if vertex not in done:
                # 큐에 넣어주고, done에도 넣어준다.
                queue.append(vertex)
                done.add(vertex)
                

# 그래프 정보
g = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2],
    5: [2]
}

search_graph(g, 2)