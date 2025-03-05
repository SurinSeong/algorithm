N = 9    # 완전 이진 트리의 정점 수
tree = [0, 33, 31, 27, 21, 22, 18, 23, 14, 19]


# 완전 이진 트리의 전위 순회
def pre_order(n, N):
    if n <= N:    # n이 실존하는 정점이면
        print(n)    # 방문
        pre_order(n*2, N)    # 왼쪽 자식으로 이동
        pre_order(n*2+1, N)    # 오른쪽 자식으로 이동

pre_order(1, N)