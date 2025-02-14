# 이분 탐색 알고리즘 with 재귀 호출
'''
1. 주어진 탐색 대상이 비어있다면 탐색할 필요 없음 (종료 조건)
2. 찾는 값과 주어진 탐색 대상의 중간 위치 값 비교
    1) 찾는 값과 중간 위치 값이 같다면 결과값으로 중간 위치 값 반환
    2) 찾는 값이 중간 위치 값보다 크다면 중간 위치의 오른쪽을 대상으로 이분 탐색 함수를 재귀 호출
    3) 찾는 값이 중간 위치 값보다 작다면 중간 위치릐 왼쪽을 대상으로 이분 탐색 함수를 재귀 호출
'''

def binary_search_with_recursion(number_list, target, start, end):
    '''
    Binary Search and Recursion
    - set search range
        - if target is found, return target's index
        - if target is not found, return -1
    '''
    # 시작 조건이 종료 조건보다 크다면 (탐색 범위 존재하지 않음)
    if start > end:
        return -1
    
    # 탐색 범위가 존재한다면
    # 중간값 저장
    middle = (start + end) // 2
    
    # 찾는 값이 더 크면, 중간값 + 1이 시작 값이 된다.
    if number_list[middle] < target:
        return binary_search_with_recursion(number_list, target, middle+1, end)

    # 찾는 값이 더 작으면, 중간값 - 1이 끝 값이 된다.
    elif number_list[middle] > target:
        return binary_search_with_recursion(number_list, target, start, middle-1)
    
    else:
        return middle
    
 
def binary_search(number_list, target):
    '''
    Call recursion function in list's all range
    '''
    return binary_search_with_recursion(number_list, target, 0, len(number_list)-1)


d = [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(binary_search(d, 36))
print(binary_search(d, 50))