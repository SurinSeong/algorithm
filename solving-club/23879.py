"""
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
"""

# 전위 순회
def pre_order(T):
    if T:
        print(T, end=' ')
        pre_order(left[T])
        pre_order(right[T])

# 트리의 정점의 총 수
V = int(input())
nodes = list(map(int, input().split()))

# 자식 노드 저장 리스트
left, right = [0]*14, [0]*14

for i in range(len(nodes)//2):
    p = nodes[i*2]
    c = nodes[i*2+1]
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c

pre_order(1)