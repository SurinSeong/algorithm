# 미로 찾기 알고리즘
# 미로의 형태와 출발점과 도착점이 주어졌을 때, 출발점에서 도착점까지 가지 위한 최단 경로를 찾는 알고리즘
'''
1. 문제 분석과 모델링
- 그래프를 이용해 미로 찾기 문제를 단계별로 모델링하기
    1) 미로 안의 공간을 정형화
    2) 이동 가능한 위치를 각각의 구역으로 나누고, 구역마다 알파벳으로 이름 붙이기
    
- 모델링한 후 문제를 다시 확인하기
    => 출발점 a에서 시작해서 벽으로 막히지 않은 위치로 차례로 이동해, 도착점 p에 이르는 가장 짧은 경로를 구하기

- 그래프 탐색 문제로 변경하기
    => 각 위치를 꼭짓점으로 만들고, 각 위치에서 벽으로 막히지 않아 이동할 수 있는 이웃한 위치를 모두 선으로 연결한다.

- 그래프를 딕셔너리로 바꾼다.
'''


maze_dict = {
    'a' : ['e'],
    'b' : ['c', 'f'],
    'c' : ['b', 'd'],
    'd' : ['c'],
    'e' : ['a', 'i'],
    'f' : ['b', 'g', 'j'],
    'g' : ['f', 'h'],
    'h' : ['g', 'l'],
    'i' : ['e', 'm'],
    'j' : ['f', 'k', 'n'],
    'k' : ['j', 'o'],
    'l' : ['h', 'p'],
    'm' : ['i', 'n'],
    'n' : ['m', 'j'],
    'o' : ['k'],
    'p' : ['l']
}


def maze(maze_dict, start, end):
    # 처리해야 할 이동 경로 큐 설정
    queue = []
    # 중복 방지 집합 설정
    done = set()
    
    # 큐에 start 넣기
    queue.append(start)
    # 집합에 start 넣기
    done.add(start)
    
    # queue에 내용이 있는 동안 반복
    while queue:
        print(queue)
        # 타겟 설정
        target = queue.pop(0)
        last = target[-1]
        
        # 목적지 도착 설정
        if last == end:
            return target
        
        for vertex in maze_dict[last]:
            if vertex not in done:
                # 큐와 집합에 vertex 넣기
                queue.append(target + vertex)
                done.add(vertex)
    
    # 빠져나갈 수 없는 미로
    return '?'
    

print(maze(maze_dict, 'a', 'p'))