# 정렬되어 있는 경우
"""
1. 자료가 오름차순으로 정렬된 상태에서 검색을 실시
2. 자료를 순차적으로 검색하면서 키 값을 비교하여, 원소의 키 값이 검색대상의 키 값보다 크면 찾는 원소가 없다는 것
"""


def seq_search_sorted(a, n, key):
    for i in range(n):
        if a[i] == key:
            return i
        elif a[i] > key:
            return -1
    return -1

