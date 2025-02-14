def same_name(name_list):
    '''
    동명이인 찾기
    - n명의 사람 이름 중 같은 이름을 찾아 집합으로 만들어 돌려주는 알고리즘
    - 딕셔너리 자료 구조 이용
    
    '''
    # 1. 각 이름이 등장하는 횟수를 저장할 빈 딕셔너리를 만든다.
    name_dict = dict()
    # 2. 입력으로 주어진 리스트에서 각 이름을 꺼내며 아래 과정을 반복
    for name in name_list:
        # 주어진 이름이 name_dict에 있는지 확인
        if name in name_dict:
            # 있다면 등장 횟수 1 증가
            name_dict[name] += 1
        else:
            # 없다면 그 이름을 키로 하는 항목을 새로 만들어 1 저장
            name_dict[name] = 1
            
    # 만들어진 딕셔너리에서 등장 횟수가 2 이상인 이름을 찾아 결과 집합에 넣은 다음 출력으로 돌려주기
    result = set()
    
    for name in name_dict:
        if name_dict[name] >= 2:
            # set에 추가하는 방법.
            result.add(name)
            
            
    return result


name = ['Tom', 'Jerry', 'Mike', 'Tom']
print(same_name(name))


'''
for 반복문을 겹쳐서 사용하지 않고 따로따로 두 번 반복하는 과정
=> O(n)
for 반복문 중첩 여부에 따라 계산 복잡도가 달라진다.
'''