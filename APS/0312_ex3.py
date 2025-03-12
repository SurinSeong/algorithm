"""
[Baby-gin]
- 여섯자리 숫자 입력 받기
- 검사
    - 숫자 3개가 연속? (run)
    - 숫자 3개가 같음? (triplet)
- 모든 순서를 봐야 함.
"""
'''
6 6 7 7 6 7
0 5 4 0 6 0
1 0 1 1 2 3
'''
def is_baby_gin():
    cnt = 0
    # run + triplet = 2

    # 앞쪽
    a, b, c = path[0], path[1], path[2]
    if a == b == c:
        cnt += 1
    elif a == (b-1) == (c-2):    # 런
        cnt += 1

    # 뒷쪽
    a, b, c = path[3], path[4], path[5]
    if a == b == c:
        cnt += 1
    elif a == (b - 1) == (c - 2):  # 런
        cnt += 1

    if cnt == 2:
        return True
    return False



def recur(cnt):
    global answer

    if cnt == 6:
        # baby-gin 여부 검사
        if is_baby_gin():
            answer = True
            return

    for idx in range(6):
        # 인덱스를 이미 사용했다면! 뽑지 말기
        if visited[idx]:
            continue

        visited[idx] = True
        path.append(arr[idx])
        recur(cnt+1)
        path.pop()
        visited[idx] = False


arr = list(map(int, input().split()))
visited = [False] * 6
path = []
answer = False

recur(0)