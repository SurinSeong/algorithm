# 주어진 리스트 안의 자료를 작은 수부터 큰 수 순서로 배열하는 정렬 알고리즘
# 정렬(sort) : 자료를 크기 순서대로 맞춰 일렬로 나열하는 것
'''
리스트에 들어있는 숫자를 크기 순으로 나열하는 정렬 알고리즘
문제 : 리스트 안에 있는 자료를 순서대로 배열
입력 : 정렬할 리스트
출력 : 순서대로 정렬된 리스트
'''
# 쉽게 설명한 선택 정렬 알고리즘
# 1. 가장 작은 숫자 찾기
def find_min_idx(number_list):
    min_idx = 0
    
    for i in range(1, len(number_list)):
        # 현재의 인덱스의 숫자가 min_idx의 숫자보다 작으면
        if number_list[i] < number_list[min_idx]:
            min_idx = i
    
    return min_idx


# 선택 정렬하기
def select_sort(number_list):
    # 선택 정렬할 새로운 리스트
    result = []
    
    # 작은 수 빼고 다시 넣고를 반복하기
    while True:
        # 숫자 리스트에 숫자가 들어있다면
        if len(number_list) > 0:
            min_idx = find_min_idx(number_list)
            # 가장 작은 숫자 빼내고 반환환
            min_number = number_list.pop(min_idx)
            # 새로운 리스트에 넣기
            result.append(min_number)
        else:
            break
    
    return result


d = [2, 4, 5, 1, 3]
print(select_sort(d))