import sys

sys.stdin = open('input.txt', 'r')

def calc(l, r, op):
    if op == '+':
        return l + r
    elif op == '-':
        return l - r
    elif op == '*':
        return l * r
    elif op == '/':
        return l / r


# DFS 하는 것 처럼! divide_and_conquer도 이렇게 리턴을 받으며 진행한다.
def post_order(v):
    # 잎 노드
    if tree[v][0] == 0 and tree[v][1] == 0:
        # 리턴
        return tree[v][2]
    # 가지 노드
    else:
        l = post_order(tree[v][0])    # l = post_order(left)
        r = post_order(tree[v][1])    # r = post_order(right)
        tree[v][2] = calc(l, r, tree[v][2])    # return l 연산 r
        return tree[v][2]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    tree = [[0]*3 for_ in range(N+1)]
    
    for i in range(N):
        temp = input().split()
        idx = int(temp[0])    # 인덱스
        # 연산자일 때
        if temp[1] == '+' or temp[1] == '-' or temp[1] == '*' or temp[1] == '/':
            tree[idx][0] = int(temp[2])
            tree[idx][1] = int(temp[3])
            tree[idx][2] = temp[1]
        # 숫자일 때
        else:
            tree[idx][2] = int(temp[1])
        
    answer = post_order(1)