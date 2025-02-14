# 이진검색 구현
# 전제 : 오름차순 정렬
def binary_search(a, n, key):   # key 를 찾으면 인덱스 반환, 실패하면 -1 반환
    start = 0
    end = n-1
    while start <= end:
        middle = (start + end) // 2
        if a[middle] == key:
            return middle
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return -1
# 재귀도 가능할 듯 하다.

