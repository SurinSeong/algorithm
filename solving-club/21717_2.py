# 줄 서는 방법 - 순열 문제
# n명의 사람이 일렬로 줄을 서고 있음.
# 1 ~ n번
# 사람의 수 : n
# 자연수 : k
# 사람을 나열하는 방법을 "사전" 순으로 함수 만들기
# 사전 순으로 k 번째를 출력



def backtrack(a, k, n, target):    # a : 순열을 통해 완성될 원소의 개수만큼의 빈 리스트, k : 현재까지 순열에 사용된 원소의 개수 (n보다 클 수 없다.), n : 순열에 사용될 총 원소의 개수
    global cnt

    c = [0] * n    # 최대 후보자 개수 만큼의 빈 리스트

    if k == n:    # 만약 모든 원소를 순열에 사용했다면

        cnt += 1

        if cnt == target:
            for i in range(0, k):    # 완성된 리스트 a의 원소를 차례로 출력한다.
                print(a[i], end=" ")
            print()

    else:    # 만약 아직 모든 원소를 순열에 사용하지 못했다면
        ncandidates = construct_candidates(a, n, k, c)    # 순열에 사용할 후보 원소들을 구성한다.

        for i in range(ncandidates):    # 후보자 개수 만큼 반복하며
            a[k] = c[i]    # 완성될 리스트의 k번째 인덱스에 넣어준다.
            backtrack(a, k + 1, n, target)    # 백트래킹




# 순열에 사용할 후보 원소들을 구성하는 함수
def construct_candidates(a, n, k, c):    # a : 순열 과정을 통해 완성될 리스트, k : 현재까지 순열에 사용된 원소의 개수, c : 후보자를 담을 리스트
    in_perm = [False] * (n + 1)    # 이미 순열에 사용된 숫자를 확인할 수 있는 boolean 리스트

    for i in range(k):    # 현재까지 순열에 사용된 원소의 개수 만큼 반복하며
        in_perm[a[i]] = True    # a에 이미 담겨 있는 원소를 인덱스로 하는 곳을 True 로 바꿔준다.

    ncandidates = 0    # 후보 리스트에 넣을 초기 인덱스
    for i in range(1, n + 1):    # 1부터 NMAX까지 반복하며
        if in_perm[i] == False:    # 만약 in_perm의 값이 False라면 (아직 순열 생성에 사용되지 않았다면)
            c[ncandidates] = i    # 후보 리스트에 넣어주기
            ncandidates += 1    # 인덱스 업데이트
    return ncandidates    # 총 몇개의 수가 업데이트 되었는지 반환


def solution(n, k):    # n : 원소 개수, k : 사전 순으로 출력했을 때의 번호
    global cnt
    # global result

    a = [0] * n  # 줄을 세우기 위한 총 원소의 개수 만큼의 리스트

    backtrack(a, 0, n, k)

    return

# MAXCANDIDATES = 3  # 줄을 세울 수 있는 최대 후보 원소 개수
# NMAX = 3  # 1부터 몇까지의 수를 세울 건지에서 몇
cnt = 0

# print(solution(3, 5))
solution(3, 5)
# print(result)
