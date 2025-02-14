# 정렬되어 있지 않은 경우의 순차 정렬
"""
1. 첫 번째 원소부터 순서대로 검색 대상과 키 값이 같은 원소가 있는지 비교하면 찾는다.
2. 키 값이 동일한 원소를 찾으면 그 원소의 인덱스를 반환한다.
3. 자료구조의 마지막에 이를 때까지 검색 대상을 찾지 못하면 검색 실패.
"""

# 찾고자 하는 원소
target = int(input())
# 숫자 데이터
data = [4, 9, 11, 23, 2, 19, 7]

def sequential_search_1(data, target):
    # 데이터 돌면서 확인하기
    for i in range(len(data)):
        if target == data[i]:
            return i
    else:
        return -1
    

def sequential_search_2(data, target):
    # while 문으로 만들어보기
    i = 0

    while (i < len(data)) and (data[i] != target):
        i += 1
        
    if i < len(data):
        return i
    else:
        return -1