# 정렬되어 있는 경우
"""
1. 자료가 오름차순으로 정렬된 상태에서 검색을 실시
2. 자료를 순차적으로 검색하면서 키 값을 비교하여, 원소의 키 값이 검색대상의 키 값보다 크면 찾는 원소가 없다는 것
"""
# 2차원 배열(NxN)일 경우

def search_number_in_2d(data, n, key):
    for i in range(n):
        for j in range(n):
            if data[i][j] > key:
                return -1
            else:
                if data[i][j] == key:
                    return [i, j]
    return -1


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

target = int(input())

print(search_number_in_2d(matrix, 3, target))
