path = []
used = [False] * 7    # 1~6 숫자 사용 여부를 기록 / 7개인 이유는 1 ~ 6을 쓰려고 (0번 인덱스를 낭비)

# 조금 더 어려운 문제의 경우 (숫자 범위가 매우 큰 경우)
# -> dict, set을 사용한다.

def recur(n):
    # 카드를 3개 뽑으면 종료
    if n == 3:
        return


cnt = 0

# 만약 카드가 1~6까지 6개가 있다면?
for num in range(1, 7):
    # 이미 num을 뽑았다면 뽑지 말기
    # == num을 뽑지 않았을 때만 뽑기

    # 방법 1
    # if num in path:    # in은 리스트 안의 요소를 모두 본다. (O(len(path)))
    #     continue

    # 방법 2
    if used[num]:    # 사용했다면 / 인덱스 검색 연산 : O(1)
        continue

    used[num] = True
    path.append(num)
    recur(cnt+1)

    used[num] = False
    path.pop()