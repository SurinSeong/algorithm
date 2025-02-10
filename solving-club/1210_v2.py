# 맨 마지막이 아니라면
    # 만약 오른쪽에 1이 있다면
    if ((0 <= j+1 < 100) and (0 <= i < 100)) and (matrix[i][j+1] == 1):
        # 어디까지 1이 있는지 찾아보기 -> 마지막 j값 받기
        # new_j = find_end_of_one(i, j, matrix, 'r')
        solve_ladder(matrix, i, j)
    # 만약 왼쪽에 1이 있다면
    elif (0 <= j-1 < 100) and (matrix[i][j-1] == 1):
        # new_j = find_end_of_one(i, j, matrix, 'l')
        solve_ladder(matrix, i, j)
    # 아래쪽에 1이 있다면 (오른쪽 왼쪽 둘다 없음)
    elif (0 <= i+1 < 100) and (matrix[i+1][j] == 1):
        solve_ladder(matrix, i+1, j)