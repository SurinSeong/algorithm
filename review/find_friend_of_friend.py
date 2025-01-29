# 기억력만으로 모든 요소를 따라가기에 무리가 있음.
# 메모를 하자!

# 1. 앞으로 처리해야 할 사람들
# -> 꼬리에 꼬리를 무는 친구의 친구들을 한 명도 빠뜨리지 않고 처리하려면
# 친구의 이름이 나올 때마다 메모지에 적어두었다가 한 명씩 처리하면서 메모지에서 지우기
# => 앞으로 처리해야 할 사람을 넣어 두었다가 하나씩 꺼내기 위한 기억 장소 : queue

# 2. 이미 추가된 사람들
# -> 친구 추적 과정에서 한 명이 여러 번 나오거나 추적이 무한 반복되지 않게 하려면
# 이미 처리 대상으로 올린 사람은 중복되지 않도록 메모지에 적어 두어야 한다.
# => 이미 처리 대상으로 추가한 사람들을 적어 둘 기억 장소 : done


def find_friend_of_friend(friend_graph, start):
    '''
    친구 관계를 이용하여 어떤 한 사람이 직접 또는 간접으로 아는 모든 친구를 출력
    '''
    print(f'{start}의 친구의 친구는?')
    # 1) 앞으로 처리할 사람을 저장할 큐
    queue = []
    # 2) 이미 큐에 추가한 사람을 저장할 집합
    done = set()
    
    # 3) 검색의 출발점이 될 사람을 큐와 집합에 추가한다.
    queue.append(start)
    done.add(start)
    
    # 4) 큐에 사람이 남아있다면 큐에서 처리할 사람을 꺼닌다.
    while queue:
        target = queue.pop(0)
        # 5) 꺼낸 사람을 출력
        print(target, end=' >> ')
        # 6) 꺼낸 사람의 친구들 중 아직 큐에 추가된 적이 없는 사람을 골라 큐와 집합에 추가
        for friend in friend_graph[target]:
            if friend not in done:
                queue.append(friend)
                done.add(friend)
        # 7) 큐에 처리할 사람이 남아 있다면 4)부터 다시 반복
    

# 파이썬으로 그래프 표현하기
# 리스트와 딕셔너리를 이용해서 그래프를 표현하는 방법
# 1. 각 꼭짓점의 정보부터 저장
# 그래프를 표현할 딕셔너리를 만들고 키로 각 꼭짓점을 지정
# 2. 키의 값으로 대응되는 꼭짓점들을 리스트에 담아준다.
friend_info = {
    'Summer' : ['John', 'Justin', 'Mike'],
    'John' : ['Summer', 'Justin'],
    'Justin' : ['John', 'Summer', 'Mike', 'May'],
    'Mike' : ['Summer', 'Justin'],
    'May' : ['Justin', 'Kim'],
    'Kim' : ['May'],
    'Tom' : ['Jerry'],
    'Jerry' : ['Tom']
}

find_friend_of_friend(friend_info, 'Summer')
print()
find_friend_of_friend(friend_info, 'Jerry')
