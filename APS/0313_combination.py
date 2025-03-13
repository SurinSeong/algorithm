"""
[도전]
- 5명 중 3명을 뽑을 수 있는 모든 경우의 수는?
"""
arr = ['A', 'B', 'C', 'D', 'E']
N = len(arr)
r = 3

# 1. 3중 for 문으로 조합 구하기
for a in range(5):
    start1 = a+1
    for b in range(start1, 5):
        start2 = b+1
        for c in range(start2, 5):
            print(arr[a], arr[b], arr[c])

# 2. 재귀 호출 (n명을 뽑는 방법은?)
path = []

def recur(cnt, start):

    if cnt == r:    # 다 찾았으면
        print(*path)    # 출력
        return

    # 후보군 찾기 -> 중복을 제거해야 한다!
    for i in range(start, N):
        path.append(arr[i])
        recur(cnt+1, i+1)    # i번째 이후부터 다시 후보 찾기 시작작
        path.pop()


recur(0, 0)