# 100 x 100
# 각 행, 각 열, 각 대각선의 합 중 최댓값

for _ in range(10):
    # 테스트 케이스 번호
    t = int(input())
    # matrix 받기
    matrix = [list(map(int, input().split())) for _ in range(100)]
    # 최대 합
    total_max_line = 0
    left_cross, right_cross = 0, 0

    # matrix 돌기
    for i in range(100):
        for j in range(100):
            # 행과 열의 인덱스가 같다면
            if i == j:
                left_cross += matrix[i][j]

            elif i == (100 - 1 - j):
                right_cross += matrix[i][j]

    i = 0
    # 행, 열별 합
    for k in range(100):
        row_sum, col_sum = 0, 0
        for j in range(100):
            col_sum += matrix[j][i+k]
            row_sum += matrix[i+k][j]

        if row_sum < col_sum:
            if total_max_line < col_sum:
                total_max_line = col_sum
        else:
            if total_max_line < row_sum:
                total_max_line = row_sum


    if left_cross < right_cross:
        if total_max_line < right_cross:
            total_max_line = right_cross
    else:
        if total_max_line < left_cross:
            total_max_line = left_cross

    print(f'#{t} {total_max_line}')