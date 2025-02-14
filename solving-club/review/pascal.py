# 재귀 함수
def pascal_triangle(row, col):  # 시간 복잡도 : O(2^n)
    # 종료 조건
    if col == 0:
        return 1
    # 대각선
    if row == col:
        return 1

    # 범위가 줄어드는 코드
    return pascal_triangle(row-1, col-1) + pascal_triangle(row-1, col)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}')

    # 파스칼 삼각형의 모든 (i, j)에 접근하기 위한 for문
    for i in range(N):
        row = []
        for j in range(i+1):
            row.append(pascal_triangle(i, j))
        print(' '.join(row))