# 친밀도 계산
# A라는 사람과 X라는 사람의 친밀도가 n이면, X의 친구 Y는 A와 친밀도가 n+1이 된다.
# => 어떤 사람의 친구들을 queue에 넣을 때, 친밀도를 1씩 증가시킴. (튜플로 처리)

def print_friend_of_friend(friend_dict, start):
    # 큐와 집합 생성
    queue = []
    done = set()
    
    # 시작 친구를 큐와 집합에 넣어주기
    queue.append((start, 0)) # 친밀도 계싼을 위해 튜플로 넣어주기
    done.add(start)
    
    # 큐에 요소가 존재하는 동안 반복
    while queue:
        # 하나씩 꺼내기
        (target, score) = queue.pop(0)
        print(target, score)
        
        for friend in friend_dict[target]:
            # 집합에 존재하지 않으면 넣어주기
            if friend not in done:
                queue.append((friend, score+1))
                done.add(friend)
                

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

print_friend_of_friend(friend_info, 'Summer')