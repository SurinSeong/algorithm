# 줄 서는 방법 - 순열 문제
# n명의 사람이 일렬로 줄을 서고 있음.
# 1 ~ n번
# 사람의 수 : n
# 자연수 : k
# 사람을 나열하는 방법을 "사전" 순으로 함수 만들기
# 사전 순으로 k 번째를 출력


# 재귀 없이 만들어보자
def backtrack_non_recursive(n):    # n : 순열에 사용될 총 원소의 개수
    # global cnt

    a = [0] * n
    c = [0] * n
    in_perm = [False] * (n + 1)    # 이미 순열에 사용된 숫자를 확인할 수 있는 boolean 리스트
    stack = []
    k = 0   # 현재까지 선택된 숫자의 개수

    while True:
        # 후보를 생성한다.
        ncandidates = construct_candidates(n, c, in_perm)

        if ncandidates == 0:    # 후보가 없다면
            if k == 0:
                break    # 종료

            k -= 1    # 하나의 자리 되돌리기
            in_perm[a[k]] = False    # 되돌린 자리에 사용된 숫자는 사용하지 않는다.
            continue

        # 후보가 있다면
        a[k] = c[0]    # 첫 번째 후보 선택하기
        in_perm[a[k]] = True    # 선택한 후보 자리를 True로 만들어주기

        if k == n - 1:    # 순열 완성
            print(' '.join(map(str, a)))
        else:    # 다른 자리 탐색
            k += 1
            stack.append(k)

        # 스택에서 탐색할 상태를 pop
        if stack:
            k = stack.pop()
        else:
            break


# 순열에 사용할 후보 원소들을 구성하는 함수
def construct_candidates(n, c, in_perm):    # a : 순열 과정을 통해 완성될 리스트, k : 현재까지 순열에 사용된 원소의 개수, c : 후보자를 담을 리스트

    ncandidates = 0    # 후보 리스트에 넣을 초기 인덱스

    for i in range(1, n + 1):    # 1부터 NMAX까지 반복하며
        if not in_perm[i]:    # 만약 in_perm의 값이 False라면 (아직 순열 생성에 사용되지 않았다면)
            c[ncandidates] = i    # 후보 리스트에 넣어주기
            ncandidates += 1

    return ncandidates

n = 3
backtrack_non_recursive(3)

