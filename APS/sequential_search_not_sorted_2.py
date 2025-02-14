# 정렬되어 있지 않은 경우의 순차 정렬
"""
1. 첫 번째 원소부터 순서대로 검색 대상과 키 값이 같은 원소가 있는지 비교하면 찾는다.
2. 키 값이 동일한 원소를 찾으면 그 원소의 인덱스를 반환한다.
3. 자료구조의 마지막에 이를 때까지 검색 대상을 찾지 못하면 검색 실패.
"""


# 2차원 배열일 경우
# 이차원 배열 - 정렬되어 있지 않을 때
def seq_number(arr, n, key):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == key:
                return 1
    return 0


# 찾고자 하는 원소
target = int(input())
# 숫자 데이터
data = [[1, 3, 2], [4, 7, 2], [9, 5, 3]]

print(seq_number(data, 3, target))
