# 선택 정렬 구현하기
# 2차원 배열
def selection_sort_in_2d(data, n):

    for i in range(, n+1):
        for j in range(1, n+1):
            if data[min_i][min_j] > data[i2][j2]:
                    min_i, min_j = i2, j2
            data[i2][j], data[min_i][min_j] = data[min_i][min_j], data[i2][j]

    return data


matrix = [
    [9, 3, 5],
    [2, 8, 1],
    [4, 6, 7]
]

print(selection_sort_in_2d(matrix, 3))
