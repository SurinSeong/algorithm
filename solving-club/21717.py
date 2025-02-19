# 줄 서는 방법 - 순열 문제
# n명의 사람이 일렬로 줄을 서고 있음.
# 1 ~ n번
# 사람의 수 : n
# 자연수 : k
# 사람을 나열하는 방법을 "사전" 순으로 함수 만들기
# 사전 순으로 k 번째를 출력


# 아래의 방법(재귀)으로는 사전순이 되지 않음.
def permutation(i, n, c, arr):
    print(f'{i}: 함수 호출 시작')
    p = arr

    c += 1
    print(c)

    if i == n:
        print(f'{i}: 함수 반환 ==>', end=' ')
        print(p)
    else:
        for j in range(i, n):
            p[i], p[j] = p[j], p[i]
            print(f'j: {j}')
            permutation(i+1, n, c, p)
            print(f'{i}: 재귀 후 (j: {j})')
            p[i], p[j] = p[j], p[i]
            print(p)


def solution(n, k):    # n : 원소 개수, k : 사전 순으로 출력했을 때의 번호
    arr = [x for x in range(1, n+1)]

    cnt = 0

    permutation(0, n, cnt, arr)


    return cnt


result = solution(3, 5)

print(result)
